# Aurora Audit

**Area:** Defensive application security and reliability tooling  
**Status:** Private repository · active development

## Purpose

Aurora Audit is a Python CLI for **authorized, read-only** audits of websites and services.
It collects configuration, security, and reliability facts without modifying the target.
Reports stay local and are designed for technical review or controlled client communication.

## Core capabilities

- Reliability, HTTP security-header, and TLS best-practice profiles.
- JSON, Markdown, HTML, and SARIF reports with redaction before output is written.
- Configuration schema validation, documented threat model, and CI audit gates.
- Bounded requests, timeouts, rate limits, and safe target handling.
- DNS/IP validation that blocks loopback, private, link-local, multicast, and reserved targets
  by default.
- Baseline comparisons and explicit ignore rules with recorded rationale.

## Security boundaries

- A written-authorization gate is required before real-target use.
- The tool does not exploit, brute-force, crawl broadly, or modify targets.
- Local target configuration and reports are ignored by Git; secrets and private keys are
  redacted from reports.

## Technical areas

Python 3.11–3.12 · CLI design · HTTP/TLS/DNS · YAML · JSON Schema · SARIF · GitHub Actions ·
pytest · pre-commit · threat modeling

## What this demonstrates

Aurora Audit is the clearest example of my security-minded development approach: define scope,
minimize data, protect the target and the operator, make reporting deterministic, and test the
safety rules themselves.
