#!/usr/bin/env python3
"""CS 450: prepare public OpenCode config; enter a key in a human terminal only."""

import argparse
from datetime import datetime, timezone
import getpass
import http.client
import json
import os
import re
from pathlib import Path
import subprocess
import sys
import tempfile
import warnings
import urllib.request
import urllib.error

MODEL = "ets:aws:us.anthropic.claude-sonnet-4-6"
BASE_URL = "https://dtcontroller.sr.unh.edu:4242/openai/v1"
WINDOWS = os.name == "nt"
MODEL_TIMEOUT = 10


def paths():
    root = Path(os.environ.get("XDG_CONFIG_HOME") or Path.home() / ".config")
    return root / "opencode" / "opencode.json", Path.home() / ".config" / "cs450-deepthought" / "api-key"


def configuration(models=None, default=MODEL):
    return {
        "$schema": "https://opencode.ai/config.json",
        "enabled_providers": ["deepthought"],
        "model": "deepthought/" + default,
        "share": "disabled",
        "provider": {"deepthought": {
            "npm": "@ai-sdk/openai-compatible",
            "name": "DeepThought",
            "options": {
                "baseURL": BASE_URL,
                "apiKey": "{file:~/.config/cs450-deepthought/api-key}",
            },
            "models": models or {MODEL: {
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


def config_targets():
    config, _ = paths()
    targets = [config]
    # Write both formats when present, so a stale JSONC cannot override the course.
    if config.with_suffix(".jsonc").exists() or config.with_suffix(".jsonc").is_symlink():
        targets.append(config.with_suffix(".jsonc"))
    custom_dir = os.environ.get("OPENCODE_CONFIG_DIR")
    if custom_dir:
        custom = Path(custom_dir).expanduser() / "opencode.json"
        targets.append(custom)
        if custom.with_suffix(".jsonc").exists() or custom.with_suffix(".jsonc").is_symlink():
            targets.append(custom.with_suffix(".jsonc"))
    custom_file = os.environ.get("OPENCODE_CONFIG")
    if custom_file:
        targets.append(Path(custom_file).expanduser())
    if os.environ.get("OPENCODE_CONFIG_CONTENT"):
        raise ValueError("OPENCODE_CONFIG_CONTENT overrides files. Unset it in this terminal, then run setup again. No files changed.")
    targets = list(dict.fromkeys(targets))
    for target in targets:
        no_links(target)
        if target.exists() and not target.is_file():
            raise ValueError("An OpenCode config path is not a file; no configuration written.")
    return targets


def write_configuration(settings):
    targets = config_targets()
    encoded = (json.dumps(settings, indent=2) + "\n").encode("utf-8")
    for config in targets:
        config.parent.mkdir(parents=True, exist_ok=True)
        if config.exists():
            original = config.read_bytes()
            if original == encoded:
                continue
            # mkstemp is exclusive, so even same-timestamp backups cannot collide.
            stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
            fd, backup = tempfile.mkstemp(prefix=config.name + ".backup-" + stamp + "-",
                                          dir=config.parent)
            with os.fdopen(fd, "wb") as output:
                if WINDOWS:
                    windows_private(Path(backup))
                output.write(original)
            print("Existing configuration backed up to: " + backup)
        temporary = None
        try:
            fd, temporary = tempfile.mkstemp(prefix=".config-", dir=config.parent)
            with os.fdopen(fd, "wb") as output:
                output.write(encoded)
            os.replace(temporary, config)
        finally:
            if temporary and os.path.exists(temporary):
                os.unlink(temporary)


def prepare():
    write_configuration(configuration())
    print("Course configuration ready. No key was read or displayed.")


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        # Never forward the Authorization header to another endpoint.
        return None


def discover_models(key):
    request = urllib.request.Request(BASE_URL + "/models",
                                     headers={"Authorization": "Bearer " + key})
    with urllib.request.build_opener(NoRedirect).open(request, timeout=MODEL_TIMEOUT) as response:
        payload = json.load(response)
    if not isinstance(payload, dict) or not isinstance(payload.get("data"), list):
        raise ValueError("Invalid model listing")
    models = {}
    for entry in payload["data"]:
        if not isinstance(entry, dict):
            raise ValueError("Invalid model entry")
        model_id = entry.get("id")
        if (not isinstance(model_id, str) or not re.fullmatch(r"[A-Za-z0-9_.:/-]+", model_id)
                or key in model_id):
            raise ValueError("Invalid model identifier")
        # OpenAI /models does not supply token limits. Avoid OpenCode's zero
        # limits for unknown IDs; these are local budgets, not advertised capacity.
        models[model_id] = {"name": "DeepThought " + model_id,
                            "limit": {"context": 32768, "output": 4096}}
        if "claude" in model_id.lower():
            models[model_id]["tool_call"] = True
            models[model_id]["limit"] = {"context": 200000, "output": 8192}
    if not models:
        raise ValueError("Empty model listing")
    return models


def select_default(models):
    # Numeric version order handles 4.10 > 4.9; IDs break ties deterministically.
    sonnets = [m for m in models if "claude" in m.lower() and "sonnet" in m.lower()]
    def version(model_id):
        numbers = [int(n) for n in re.findall(r"\d+", model_id)]
        versions = tuple(n for n in numbers if n < 10000)
        dates = tuple(n for n in numbers if n >= 10000)
        return versions, dates, model_id
    return max(sonnets, key=version) if sonnets else sorted(models)[0]


def refresh_models(*, preserve_on_failure=True):
    config_targets()  # Validate destinations before reading the stored credential.
    _, key_file = paths()
    no_links(key_file)
    if not key_file.is_file():
        raise ValueError("No saved key. Run the key action yourself in a normal terminal first.")
    key = key_file.read_text(encoding="utf-8")
    if not key or any(c.isspace() or not c.isprintable() for c in key):
        raise ValueError("Saved key is invalid. Run the key action again; do not display the file.")
    try:
        models = discover_models(key)
    except (OSError, ValueError, urllib.error.URLError, http.client.HTTPException):
        # Never echo server bodies or exception details; they may reflect the key.
        if preserve_on_failure:
            print("Model discovery unavailable. Existing configuration left unchanged.")
        else:
            write_configuration(configuration())
            print("Model discovery unavailable. Using fallback: DeepThought Claude Sonnet 4.6.")
        return
    default = select_default(models)
    write_configuration(configuration(models, default))
    print("DeepThought models discovered: " + str(len(models)))
    print("Default model: deepthought/" + default)
    print("Default choice: highest numeric Claude Sonnet version; otherwise first model ID alphabetically.")


def windows_private(path, directory=False):
    # Reset old explicit grants, then protect the object for the current SID.
    import csv
    result = subprocess.run(["whoami", "/user", "/fo", "csv", "/nh"],
                            capture_output=True, text=True, check=True)
    try:
        sid = next(csv.reader(result.stdout.splitlines()))[1]
    except (IndexError, StopIteration):
        raise ValueError("Could not identify the Windows account; no key saved.") from None
    if not re.fullmatch(r"S-1-(?:[0-9]+-)*[0-9]+", sid):
        raise ValueError("Could not identify the Windows account; no key saved.")
    grant = "*" + sid + (":(OI)(CI)F" if directory else ":F")
    subprocess.run(["icacls", str(path), "/reset"], capture_output=True, check=True)
    subprocess.run(["icacls", str(path), "/inheritance:r", "/grant:r", grant],
                   capture_output=True, check=True)


def private_directory(directory):
    no_links(directory)
    directory.mkdir(parents=True, exist_ok=True, mode=0o700)
    if WINDOWS:
        windows_private(directory, directory=True)
    else:
        directory.chmod(0o700)


def enter_key():
    if not sys.stdin.isatty() or not sys.stdout.isatty():
        raise ValueError("Run key entry yourself in a normal terminal, outside the agent. Piped input is refused.")
    config_targets()
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
    print("Key saved privately. Its value was not printed.")
    refresh_models(preserve_on_failure=False)
    print("You can now open OpenCode.")


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
    parser.add_argument("action", choices=["prepare", "key", "check", "refresh-models"])
    args = parser.parse_args()
    try:
        if args.action == "prepare":
            prepare()
        elif args.action == "key":
            enter_key()
        elif args.action == "refresh-models":
            refresh_models()
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
