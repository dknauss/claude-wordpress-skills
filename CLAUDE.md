# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository currently ships one Claude Code skill, `wp-performance-review`, plus two slash commands that invoke it. The focus is WordPress performance review for themes, plugins, and custom code.

## Repository Structure

```
.claude-plugin/           # Plugin configuration
  plugin.json             # Plugin metadata (name, version, author)
  marketplace.json        # Marketplace registration

skills/                   # Skill definitions
  wp-performance-review/
    SKILL.md              # Main skill file with YAML frontmatter
    references/           # Supporting documentation
      anti-patterns.md    # PHP code anti-patterns reference
      wp-query-guide.md   # WP_Query optimization reference
      caching-guide.md    # Caching strategies reference
      measurement-guide.md # Performance measurement reference

commands/                 # Slash command definitions
  wp-perf-review.md       # Full performance review command
  wp-perf.md              # Quick triage scan command
```

## Adding New Skills

1. Create directory: `skills/wp-your-skill/`
2. Create `SKILL.md` with YAML frontmatter:
   ```yaml
   ---
   name: skill-name
   description: Trigger phrases and when to use. Max 1024 chars.
   ---
   ```
3. Add references in `skills/wp-your-skill/references/` if needed
4. Update `README.md` and `CONTRIBUTING.md` to document the new skill
5. Run `python3 scripts/validate_repo.py`

Note: while `.claude-plugin/marketplace.json` points to the repository root (`"./"`), adding a new skill does not require a per-skill marketplace entry.

## Adding Slash Commands

Create a markdown file in `commands/` with:
```yaml
---
description: What the command does
argument-hint: [optional-args]
---
```

## Code Standards

PHP examples must follow WordPress PHP Coding Standards:
- Spaces inside parentheses: `function_name( $arg )`
- Use `array()` not `[]`
- Yoda conditions: `if ( true === $value )`
- Snake_case for variables/functions
- Prefix custom functions: `prefix_function_name()`

Use consistent severity labels in skill content:
- **CRITICAL**: Will cause failures at scale (OOM, 500 errors)
- **WARNING**: Degrades performance under load
- **INFO**: Optimization opportunity

## Testing Changes

```bash
# Copy skill to Claude skills directory for testing
cp -r skills/your-skill ~/.claude/skills/

# Restart Claude Code to load changes

# Validate repository metadata and docs
python3 scripts/validate_repo.py
```

## Versioning

Update version in both files when releasing:
- `.claude-plugin/plugin.json` - `version` field
- `.claude-plugin/marketplace.json` - `metadata.version` field
