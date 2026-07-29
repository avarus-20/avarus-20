# WordPress Care Report

**Area:** WordPress maintenance, website health, and client reporting  
**Status:** Private repository · beta-stage active development

## Purpose

WordPress Care Report is a defensive Python CLI that creates a client-friendly health report
for an **authorized** WordPress installation. It supports a repeatable freelance workflow:
inspect first, explain findings clearly, propose a safe next step, and never change a client
site without separate approval.

## Core capabilities

- Read-only local inspection of WordPress core, plugins, themes, mu-plugins, selected
  wp-config.php hygiene signals, debug-log hygiene, and backup-like files.
- Optional inspection of one authorized public URL for basic security headers and cookie
  attributes.
- HTML client report plus optional JSON; secrets and raw sensitive values are not displayed.
- Deterministic report ordering and clear finding severities for manual review.
- Safe URL handling: unsupported schemes, private/loopback targets, userinfo, and unsafe
  redirects are blocked or redacted.
- Scan reports cannot be written inside the scanned WordPress root.

## Explicit limitations

This is not a penetration-test, exploit, brute-force, crawler, CVE-database, or automatic-fix
tool. A finding is a signal for review, not a guarantee that a site is secure or insecure.

## Technical areas

Python · Typer · Jinja2 · Rich · pytest · Ruff · WordPress · WP-CLI · report generation ·
SSRF-aware URL validation · privacy-safe output

## What this demonstrates

The project connects development and client work: safe technical checks are turned into a
clear, bounded service that a small-business owner can understand and approve.
