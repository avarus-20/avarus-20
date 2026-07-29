# WordPress Maintenance Lab

**Area:** WordPress operations, recovery, and safe freelance delivery  
**Status:** Private controlled lab · active development

## Purpose

WordPress Maintenance Lab is a controlled environment for practicing and documenting
low-risk WordPress maintenance before applying a workflow to a client site. It supports the
service process behind WordPress Care Report rather than pretending that a generated report is
enough by itself.

## Focus areas

- Safe updates with a documented rollback plan.
- Backup, restore, and migration verification.
- Plugin and theme diagnostics in local or staging environments.
- Basic performance and security maintenance checks.
- Plain-language maintenance reports for non-technical clients.
- Repeatable delivery checklists: authorization → backup → staged change → test → report →
  handover.

## Technical foundations

Ubuntu Linux · Docker · DDEV · WordPress · WP-CLI · Git · GitHub · Markdown-based reporting

## Safety boundaries

No live client website is connected to the lab. Work is performed only on owned or explicitly
authorized systems; passwords, exports, database dumps, backups, and customer data are never
committed.

## What this demonstrates

The lab shows that my WordPress work is built around recovery and verification, not quick,
untracked changes on a live production website.
