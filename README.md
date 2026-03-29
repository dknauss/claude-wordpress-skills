# Claude WordPress Skills

> **Note:** The canonical source for all WordPress agent skills is [dknauss/agent-skills](https://github.com/dknauss/agent-skills) (fork of [WordPress/agent-skills](https://github.com/WordPress/agent-skills)). The `wp-performance-review` skill has been migrated there. This repo is maintained as a public fork of [elvismdev/claude-wordpress-skills](https://github.com/elvismdev/claude-wordpress-skills) but is no longer the primary distribution point.

WordPress-focused skills for [Claude Code](https://claude.ai/code), currently centered on performance review for plugins, themes, and custom code.

## Shipped Skills

| Skill | Description | Status |
|-------|-------------|--------|
| **wp-performance-review** | Performance code review and optimization analysis | ✅ |

## Planned Skills

- `wp-security-review`
- `wp-gutenberg-blocks`
- `wp-theme-development`
- `wp-plugin-development`

## Installation

### Option 1: Clone Locally

Install the repository as a local Claude plugin:

```bash
git clone https://github.com/elvismdev/claude-wordpress-skills.git ~/.claude/plugins/wordpress
```

The repository includes `.claude-plugin/` manifests for clients that support plugin-style installs from a repository checkout.

### Option 2: Add to Project

```bash
# In your project root
git submodule add https://github.com/elvismdev/claude-wordpress-skills.git .claude/plugins/wordpress
git commit -m "Add WordPress Claude skills"
```

Team members get the skills automatically when they clone or update the repo.

### Option 3: Copy Individual Skills

Download and extract specific skills:

```bash
# Copy just the performance review skill
cp -r skills/wp-performance-review ~/.claude/skills/
```

## Slash Commands

When the repository is installed as a plugin, these commands become available:

| Command | Description |
|---------|-------------|
| `/wp-perf-review [path]` | Full WordPress performance code review with detailed analysis and fixes |
| `/wp-perf [path]` | Quick triage scan using grep patterns (fast, critical issues only) |

### Usage Examples

```bash
# Full review of current directory
/wp-perf-review

# Full review of specific plugin
/wp-perf-review wp-content/plugins/my-plugin

# Quick scan of a theme (fast triage)
/wp-perf wp-content/themes/my-theme

# Quick scan to check for critical issues before deploy
/wp-perf .
```

### Command Comparison

| Aspect | `/wp-perf-review` | `/wp-perf` |
|--------|-------------------|------------|
| **Speed** | Thorough (slower) | Fast triage |
| **Depth** | Full analysis + fixes | Critical patterns only |
| **Output** | Grouped by severity with line numbers | Quick list of matches |
| **Use case** | Code review, PR review, optimization | Pre-deploy check, quick audit |

## Natural Language Usage

Skills also activate automatically based on context. Just ask naturally:

```
Review this plugin for performance issues
Audit this theme for scalability problems
Check this code for slow database queries
Help me optimize this WP_Query
Check my theme before launch
Find anti-patterns in this plugin
```

Claude will detect the context and apply the appropriate skill.

### Trigger Phrases

| Skill | Trigger Phrases |
|-------|-----------------|
| wp-performance-review | "performance review", "optimization audit", "slow WordPress", "slow queries", "scale WordPress", "high-traffic", "code review", "before launch", "anti-patterns", "timeout", "500 error", "out of memory" |

## What's Included

### wp-performance-review

Comprehensive performance code review covering:

- **Database Query Anti-Patterns** - Unbounded queries, unvalidated IDs, slow LIKE patterns, large exclusion-list pitfalls
- **Hooks & Actions** - Expensive code on init, database writes on page load, inefficient hook placement
- **Caching Issues** - Uncached function calls, object cache patterns, transient best practices
- **AJAX & External Requests** - admin-ajax.php alternatives, polling patterns, HTTP timeouts
- **Template Performance** - N+1 queries and heavy work inside loops
- **PHP Code Patterns** - in_array() performance, heredoc escaping issues
- **JavaScript Bundles** - Full library imports, defer/async strategies
- **Block Editor** - heavy editor previews, expensive data fetching, InnerBlocks handling
- **Platform Guidance** - Patterns for WordPress VIP, WP Engine, Pantheon, self-hosted

Output includes severity levels (Critical/Warning/Info) with line numbers and fix recommendations.

## Requirements

- [Claude Code](https://claude.ai/code) CLI installed
- Skills are loaded automatically - no additional dependencies
- Python 3 if you want to run the repository validator locally

## Validation

Run the repository checks before opening a PR:

```bash
python3 scripts/validate_repo.py
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

Ways to contribute:

- Report issues or incorrect/deprecated advice
- Suggest new anti-patterns or best practices
- Improve documentation or examples
- Submit new skills

## License

MIT License — see [LICENSE](LICENSE) for details.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history.

---

**Note**: These skills reflect practical WordPress performance-review guidance, not universal rules. Prefer measured evidence and platform-specific constraints over blanket heuristics, and open an issue when advice here stops matching current WordPress behavior.
