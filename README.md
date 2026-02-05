# pmprompt (Claude Code plugin)

Public plugin for Claude Code that packages **product management skills** backed by pmprompt.

## Structure

- `.claude-plugin/plugin.json` — plugin manifest
- `skills/` — agent skills (each skill is a folder with `SKILL.md`)

## Development

Test locally:

```bash
claude --plugin-dir .
```

Then run:

- `/pmprompt:<skill-name>`

## Notes

This repo intentionally contains **no internal operating workflows** (no private content ops, IDs, or tokens).
