# MCP server: install and configure

The ASO skill ships an MCP server that exposes seven analyzer tools to
any MCP-aware client (Claude Desktop, Cursor, Continue, custom agents).
You don't need Claude Code for this — only Python and the `mcp` package.

## What you get

Seven MCP tools, all wrapping existing `aso_skill` functions:

| Tool | What it does |
|---|---|
| `aso_score` | ASO health score (0-100) across four dimensions |
| `aso_optimize` | Generate platform-validated title / description / keywords |
| `aso_validate` | Check a single field against Apple / Google char limits |
| `aso_analyze_keywords` | Rank a keyword set by ASO potential |
| `aso_plan_ab_test` | Design an A/B test with proper sample size |
| `aso_itunes_search` | Cached iTunes Search API |
| `aso_itunes_app` | Fetch one app by its App Store ID |

All tool inputs and outputs are JSON. The schemas are auto-generated
from the Python type hints and docstrings, so any compliant MCP client
can discover and call them.

## Install

```bash
pip install 'aso-skill[mcp]'
```

That pulls in the `mcp` SDK alongside the skill. The console script
`aso-mcp` is now on your PATH:

```bash
aso-mcp --help    # FastMCP's stdio server help
```

## Claude Desktop

Drop this into `claude_desktop_config.json` (location varies by OS — see
[Anthropic's docs](https://docs.anthropic.com/en/docs/build-with-claude/computer-use)):

```json
{
  "mcpServers": {
    "aso-skill": {
      "command": "aso-mcp"
    }
  }
}
```

Restart Claude Desktop. The seven tools appear in the tool picker.

If `aso-mcp` isn't on your PATH (virtualenv install, etc.), use the
explicit form:

```json
{
  "mcpServers": {
    "aso-skill": {
      "command": "/full/path/to/python",
      "args": ["-m", "aso_skill.mcp_server"]
    }
  }
}
```

## Cursor / Continue / custom MCP clients

The server speaks MCP over stdio. Configure your client to spawn
`aso-mcp` (or `python -m aso_skill.mcp_server`) — the exact config
format depends on the client.

## Example session

Once configured, asking Claude Desktop something like

> "Score this app's ASO health: it has rating 4.6 with 8500 ratings, 6 keywords in top 10, conversion 6% with 12k downloads last month and trending up. Title uses 2 keywords at 28 chars, description is 2200 chars with 0.8 quality and keyword density of 4.5."

…now calls `aso_score` directly instead of relying on the model to
hand-roll the math.

## Troubleshooting

- **`aso-mcp` not found**: ensure `pip install 'aso-skill[mcp]'` finished
  successfully and that the install location is on your PATH.
- **Claude Desktop doesn't see the tools**: check the desktop logs at
  `~/Library/Logs/Claude/mcp.log` (macOS) for startup errors.
- **iTunes calls fail**: the server uses the cached iTunes wrapper from
  `aso_skill.itunes`. Set `ASO_ITUNES_NO_CACHE=1` to bypass the cache,
  or clear it via `aso itunes --clear-cache`.
