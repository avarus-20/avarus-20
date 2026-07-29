# Multilingual Web QA

**Area:** Website quality assurance, localization, and safe web checks  
**Status:** Private repository · portfolio v1

## Purpose

Multilingual Web QA is a read-only Python CLI for technical checks on Finnish and English variants of a website. It starts with synthetic localhost fixtures so the workflow can
be tested safely before any real-site audit is considered.

## What it checks

- Broken same-host links and redirects.
- Links that point outside the audited host.
- Missing, incomplete, or non-reciprocal hreflang sets.
- Missing x-default, canonical URLs, titles, or meta descriptions.
- Duplicate titles and html lang mismatches.
- Basic form-markup issues without submitting forms.

## Safety boundaries

- No POST, PUT, PATCH, or DELETE requests.
- No login, cookies, tokens, .env reads, WordPress changes, or database changes.
- The crawler stays within the configured scheme, host, and port and has page/time limits.
- Non-localhost use is blocked by default and requires explicit authorization.

## Technical areas

Python 3.11–3.12 · CLI tooling · HTML metadata · localization QA · hreflang · canonical URLs ·
pytest · Ruff · mypy · deterministic JSON/Markdown reports

## What this demonstrates

This tool turns multilingual website knowledge into repeatable QA. It is especially relevant to
small businesses that need clear Finnish and English page variants without silently breaking search,
navigation, or forms.
