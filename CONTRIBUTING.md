# Contributing to WordPress Claude Skills

Thank you for your interest in contributing! This guide will help you get started.

## Ways to Contribute

### 🐛 Report Issues

Found a problem? Open an issue with:

- **Skill name** — Which skill has the issue
- **Description** — What went wrong or what advice was incorrect
- **Expected behavior** — What should have happened
- **Code example** — If applicable, share the code that triggered the issue

### 💡 Suggest Improvements

Have an idea? Open an issue with:

- **Anti-pattern or best practice** — Describe the pattern
- **Why it matters** — Performance impact, security risk, etc.
- **Code examples** — Show BAD and GOOD examples
- **Sources** — Links to documentation or benchmarks (optional)

### 📝 Improve Documentation

- Fix typos or unclear explanations
- Add more code examples
- Improve the README or skill descriptions

### 🔧 Submit New Skills

Want to create a new WordPress skill? See [Creating a New Skill](#creating-a-new-skill) below.

## Development Setup

1. **Fork and clone** the repository:

   ```bash
   git clone https://github.com/elvismdev/claude-wordpress-skills.git
   cd claude-wordpress-skills
   ```

2. **Create a branch** for your changes:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Test your changes** by copying to your Claude skills directory:

   ```bash
   cp -r skills/your-skill ~/.claude/skills/
   ```

4. **Run the repository validator**:

   ```bash
   python3 scripts/validate_repo.py
   ```

5. **Restart Claude Code** to load the updated skill.

## Skill Structure

Each skill follows this structure:

```
skills/skill-name/
├── SKILL.md              # Required: Main skill file with YAML frontmatter
└── references/           # Optional: Supporting documentation
    ├── guide-one.md
    └── guide-two.md
```

### SKILL.md Requirements

```markdown
---
name: skill-name
description: What this skill does and when Claude should use it. Include trigger phrases.
---

# Skill Title

Brief introduction.

## Section One

Content with code examples...
```

**Frontmatter rules:**

- `name`: lowercase with hyphens, max 64 characters
- `description`: max 1024 characters, include trigger phrases

### Code Example Standards

All PHP code must follow [WordPress PHP Coding Standards](https://developer.wordpress.org/coding-standards/wordpress-coding-standards/php/):

```php
// ✅ GOOD: WordPress coding standards
$query = new WP_Query(
    array(
        'post_type'      => 'post',
        'posts_per_page' => 10,
        'no_found_rows'  => true,
    )
);

if ( $query->have_posts() ) {
    while ( $query->have_posts() ) {
        $query->the_post();
        // Process post.
    }
}
wp_reset_postdata();
```

Key standards:

- Spaces inside parentheses: `function_name( $arg )`
- Use `array()` not `[]` for arrays
- Yoda conditions: `if ( true === $value )`
- Snake_case for variables and functions
- Prefix custom functions: `prefix_function_name()`

### Severity Levels

Use consistent severity labels:

| Level | Use For |
|-------|---------|
| **CRITICAL** | Will cause failures at scale (OOM, 500 errors, DB locks) |
| **WARNING** | Degrades performance under load |
| **INFO** | Optimization opportunity, nice-to-have |

### Comment Style

```php
// ❌ BAD: Description of the problem.
bad_code_example();

// ✅ GOOD: Description of the solution.
good_code_example();
```

## Creating a New Skill

1. **Create the directory structure**:

   ```bash
   mkdir -p skills/wp-your-skill/references
   ```

2. **Create SKILL.md** with proper frontmatter and content.

3. **Add references** if the skill needs supporting documentation.

4. **Update README.md** to list the new skill.

5. **Run `python3 scripts/validate_repo.py`**.

6. **Test thoroughly** before submitting.

While `.claude-plugin/marketplace.json` points to the repository root (`"./"`), new skills do not need individual marketplace entries unless the packaging model changes.

## Pull Request Process

1. **Ensure your code follows** the standards above.

2. **Update documentation** if you've changed functionality.

3. **Add a changelog entry** in CHANGELOG.md under "Unreleased".

4. **Run `python3 scripts/validate_repo.py`**.

5. **Submit the PR** with a clear description of changes.

6. **Respond to feedback** — we may ask for adjustments.

## Code of Conduct

- Be respectful and constructive
- Focus on the technical merits
- Help others learn and improve

## Questions?

Open an issue with the "question" label, and we'll help you out.

---

Thank you for contributing to better WordPress development! 🎉
