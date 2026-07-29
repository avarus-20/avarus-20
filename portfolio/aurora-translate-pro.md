# Aurora Translate Pro

**Area:** Document-processing workflows, web development, and privacy-aware integrations  
**Status:** Private repository · active development

## Purpose

Aurora Translate Pro is a document-translation service prototype for professional text and
document workflows. It supports single-file and batch processing while keeping provider
credentials and document-provider identifiers on the server side.

## Engineering focus

- FastAPI-based backend and a web frontend for controlled file workflows.
- TXT, DOCX, and PDF processing modes, including layout-preservation flows where supported.
- Provider abstraction with mock providers for development and tests before any paid API use.
- Job status, download flow, batch ZIP output, and optional quality-assurance reports.
- Limits on file count, file size, text size, and job lifetime.

## Security and privacy practices

- API keys are environment-based and never committed.
- Provider document keys remain server-side.
- Document contents and provider exceptions are not exposed in browser logs.
- Health endpoints expose only non-secret public configuration.
- Test workflows run with mock providers and do not need live keys.

## What this demonstrates

This project shows web-service design around a sensitive workflow: user uploads, third-party
providers, background-style job state, safe downloads, cost control, and data-minimization
decisions.
