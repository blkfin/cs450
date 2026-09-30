# CS 450 L10 · Build something real with an agent

- Course: CS 450 · AI and the World
- Lecture: L10 / Build something real with an agent
- Semantic source: `lecture.resolved.json`
- Semantic source SHA-256: `46ae2fd53bd2f59b4bcc6cacb527e7a728cff65d4bc08ffae6234c1ef1a987b6`
- Schema: `lecture/v1`

Normalized reader semantics, projected per block type from the resolved lecture document. Layout classes, presenter chrome, SVG drawing instructions and instructor-only fields are not part of this projection — they were never built.

## iClicker 0 · What has happened so far?

- Source lineage: `cs450-fall-2026-l10-real-agent#sections.c01`
- Citations: `approved_storyboard`

- **Requested action**: Read the contents of index.html
- **Status**: The tool has not run yet.

What has happened so far?

1. A · The model has already read the file
2. B · The model has asked software to read the file
3. C · The model has created a new file
4. D · The model has asked the student to read it aloud

The displayed request is a plain-English translation of a tool call, not Cursor syntax.

## One turn can contain several cycles

- Source lineage: `cs450-fall-2026-l10-real-agent#sections.c02`
- Citations: `approved_storyboard`

### Diagram explanation

One user turn carries a goal through several internal cycles to a result the user can check.

- YOUR GOAL leads to cycle 1
- cycle 1 leads to cycle 2
- cycle 2 leads to cycle 3
- cycle 3 leads to RESULT

- **Cycle**: Decide, request an action, read the result, then repeat, answer, or stop for help.
- **Turn**: Everything from your request to the agent's answer.

### A tool call asks surrounding software to do something. The result says what happened.

## Capabilities, permissions, and your role

- Source lineage: `cs450-fall-2026-l10-real-agent#sections.c03`
- Citations: `approved_storyboard`

### MODEL

- Chooses an available tool
- Supplies the tool's inputs

### CURSOR SOFTWARE

- Can read files · write files · run commands
- Checks permission; some actions wait for your approval

## Set up · Step 1: install

- Source lineage: `cs450-fall-2026-l10-real-agent#sections.c04`
- Citations: `approved_storyboard`

Copy from the Canvas handout. Run any PATH-update line the installer prints.

Paste into your Agate terminal

```bash
curl https://cursor.com/install -fsS | bash
```

## Set up · Step 2: log in

- Source lineage: `cs450-fall-2026-l10-real-agent#sections.c05`
- Citations: `approved_storyboard`, `cursor_auth`

Open the printed link on your laptop, sign in, then return to Agate.

Make login print a link

```bash
NO_OPEN_BROWSER=1 agent login
```

## Set up · Step 3: start the agent

- Source lineage: `cs450-fall-2026-l10-real-agent#sections.c06`
- Citations: `approved_storyboard`

Prompt visible? You're ready. Stuck? Pair with a neighbour whose agent is ready.

Start Cursor's terminal agent

```bash
agent
```

## Three rules before the agent changes files

- Source lineage: `cs450-fall-2026-l10-real-agent#sections.c07`
- Citations: `approved_storyboard`, `cursor_pricing`

- **Public**: No full name, photo, student ID, or anything personal.
- **Limited**: The free plan limits requests; today should take two to four.
- **Approval**: Read before approving; ask if you do not understand a command.

## Build hello world together, then verify it

- Source lineage: `cs450-fall-2026-l10-real-agent#sections.c08`
- Citations: `approved_storyboard`

Result: the page. Boundaries: HTML/CSS, no install, other files unchanged. Check: open the public address.

Paste this goal into the agent

```text
Create a page that displays “Hello, CS 450!” at
~/public_html/cs450/index.html. Use HTML and CSS; install no software.
Keep my other files unchanged. If the web server cannot read the page,
explain the permission change you propose before making it.
Tell me the page's public address so I can open it and check it.
```

Loading checks publication. Matching the request checks the result.

Check it yourself in a browser

```text
https://www.cs.unh.edu/~YOUR-USERNAME/cs450/
```

## Who did which part?

- Source lineage: `cs450-fall-2026-l10-real-agent#sections.c08b`
- Citations: `approved_storyboard`

### Model

- Created content; requested file actions

### Cursor tools

- Saved the file

### UNH server

- Served the page

### You

- Checked address and content

## Your turn · Make your participation page

- Source lineage: `cs450-fall-2026-l10-real-agent#sections.c09`
- Citations: `approved_storyboard`

Test it. Report the expected behavior, then report the observed behavior.

Personalize the brackets, then paste

```text
Create a new page at ~/public_html/cs450/l10.html.
Start from my hello page. Use [a dark background and large headings,
or my design choice]. Add [a public topic I choose]. Keep index.html
unchanged. Use only HTML and CSS; install nothing. Make it web-readable
and give me the public address.
```

Credit = the URL loads and the page differs from hello world.

Submit this URL on Canvas

```text
https://www.cs.unh.edu/~YOUR-USERNAME/cs450/l10.html
```

## If the page does not load, diagnose the visible result

- Source lineage: `cs450-fall-2026-l10-real-agent#sections.c09b`
- Citations: `approved_storyboard`

| You see | Do this |
| --- | --- |
| agent: command not found | Log out of Agate, log back in, and try again |
| 403 Forbidden | Ask the agent to fix permissions so the web server can read the page |
| 404 Not Found | Check your username and the cs450 folder name |
| Stuck after five minutes | Pair up; submit your URL by Friday |

## iClicker 1 · Who paid for your pages?

- Source lineage: `cs450-fall-2026-l10-real-agent#sections.c10`
- Citations: `approved_storyboard`, `cursor_pricing`

Your pages cost you nothing. Who paid for the computing behind them?

1. A · Nobody; it is free
2. B · Cursor, which provided the agent service
3. C · UNH, which runs Agate and the web server
4. D · Both B and C

Free to you is not free to run.

- Friday: build a small interactive app, test it, fix one concrete problem, and share the URL plus what you learned.
- Coming up: model choice, usage limits, and UNH's AI service.
