#!/usr/bin/env python3
"""CS 450: prepare public OpenCode config; enter a key in a human terminal only."""

import argparse
import getpass
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import warnings

MODEL = "ets:aws:us.anthropic.claude-sonnet-4-6"


def paths():
    root = Path.home() / ".config"
    return root / "opencode" / "opencode.json", root / "cs450-deepthought" / "api-key"


def configuration():
    return {
        "$schema": "https://opencode.ai/config.json",
        "enabled_providers": ["deepthought"],
        "model": "deepthought/" + MODEL,
        "share": "disabled",
        "provider": {"deepthought": {
            "npm": "@ai-sdk/openai-compatible",
            "name": "DeepThought",
            "options": {
                "baseURL": "https://dtcontroller.sr.unh.edu:4242/openai/v1",
                "apiKey": "{file:~/.config/cs450-deepthought/api-key}",
            },
            "models": {MODEL: {
                "name": "DeepThought Claude Sonnet 4.6",
                "tool_call": True,
                "limit": {"context": 200000, "output": 8192},
            }},
        }},
    }


def no_links(path):
    # Refuse symlinked destinations and ancestors before touching secrets/config.
    if any(p.is_symlink() for p in [path, *path.parents]):
        raise ValueError("A setup path is a symlink; stop and ask your instructor.")


def prepare():
    config, _ = paths()
    no_links(config)
    # JSONC and alternate config locations need a deliberate review, not replacement.
    if any(os.environ.get(v) for v in (
        "OPENCODE_CONFIG", "OPENCODE_CONFIG_DIR", "XDG_CONFIG_HOME", "OPENCODE_CONFIG_CONTENT"
    )) or config.with_suffix(".jsonc").exists():
        raise ValueError("An alternate OpenCode configuration exists; ask your instructor before changing it.")
    expected = configuration()
    if config.exists():
        try:
            matches = json.loads(config.read_text(encoding="utf-8")) == expected
        except (ValueError, UnicodeError):
            matches = False
        if not matches:
            raise ValueError("Existing OpenCode configuration differs. It was left untouched; ask your instructor.")
    else:
        config.parent.mkdir(parents=True, exist_ok=True)
        with config.open("x", encoding="utf-8") as output:
            output.write(json.dumps(expected, indent=2) + "\n")
    print("Course configuration ready. No key was read or displayed.")


def private_directory(directory):
    no_links(directory)
    if os.name == "nt" and directory.exists():
        raise ValueError("Windows key folder already exists. Ask your instructor before replacing or repairing it.")
    directory.mkdir(parents=True, exist_ok=True, mode=0o700)
    if os.name == "nt":
        # Protect the directory before creating a key; new files inherit this ACL.
        # Use the current SID so localized Windows account names do not matter.
        result = subprocess.run(["whoami", "/user", "/fo", "csv", "/nh"],
                                capture_output=True, text=True, check=True)
        import csv
        sid = next(csv.reader(result.stdout.splitlines()))[1]
        if not sid.startswith("S-1-"):
            raise ValueError("Could not identify the Windows account; no key saved.")
        subprocess.run(["icacls", str(directory), "/inheritance:r", "/grant:r",
                        "*" + sid + ":(OI)(CI)F"], capture_output=True, check=True)
    else:
        directory.chmod(0o700)


def enter_key():
    if not sys.stdin.isatty() or not sys.stdout.isatty():
        raise ValueError("Run key entry yourself in a normal terminal, outside the agent. Piped input is refused.")
    config, key_file = paths()
    no_links(config)
    if not config.exists():
        raise ValueError("Run prepare first; no key was saved.")
    no_links(key_file)
    private_directory(key_file.parent)
    # Treat getpass's echoing fallback as an error, never as permission to echo.
    with warnings.catch_warnings():
        warnings.simplefilter("error", getpass.GetPassWarning)
        key = getpass.getpass("Paste your DeepThought key (hidden), then press Enter: ")
    if not key or any(c.isspace() or not c.isprintable() for c in key):
        raise ValueError("Key must be nonempty, with no whitespace or control characters. Nothing saved.")
    temporary = None
    try:
        fd, temporary = tempfile.mkstemp(prefix=".key-", dir=key_file.parent)
        with os.fdopen(fd, "w", encoding="utf-8") as output:
            output.write(key)
        os.replace(temporary, key_file)
    finally:
        if temporary and os.path.exists(temporary):
            os.unlink(temporary)
    print("Key saved privately. Its value was not printed. You can now open OpenCode.")


def check():
    config, key_file = paths()
    no_links(config)
    no_links(key_file)
    # Do not open the key. This checks presence, not validity with DeepThought.
    config_ok = config.is_file()
    key_ok = key_file.is_file() and key_file.stat().st_size > 0
    print("Configuration: " + ("present" if config_ok else "missing"))
    print("Key file: " + ("present" if key_ok else "missing"))
    print("DeepThought connection: not tested")
    return 0 if config_ok and key_ok else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["prepare", "key", "check"])
    args = parser.parse_args()
    try:
        if args.action == "prepare":
            prepare()
        elif args.action == "key":
            enter_key()
        else:
            return check()
    except ValueError as error:
        # Only our fixed validation messages reach here; never include key input.
        print(str(error), file=sys.stderr)
        return 1
    except (OSError, getpass.GetPassWarning, subprocess.SubprocessError,
            EOFError, KeyboardInterrupt):
        # Never print exception details: they can contain filesystem or input data.
        print("Setup stopped safely. No secret is shown. Check prerequisites or ask your instructor.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
