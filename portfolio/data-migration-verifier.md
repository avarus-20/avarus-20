# Data Migration Verifier

**Area:** Python, SQL data quality, and privacy-safe reporting  
**Status:** Private repository · portfolio demonstration under active development

## Purpose

Data Migration Verifier is a Python CLI that checks whether a SQL data migration can be
described as successful. The portfolio implementation compares synthetic local SQLite data and
also has a read-only MySQL/MariaDB path for local synthetic databases.

## What it verifies

- Source and target row counts.
- Keys missing from the target and unexpected target keys.
- Differences in selected business columns.
- Duplicate keys discovered while reading.

## Data-safety design

- SQLite databases are opened read-only.
- MySQL/MariaDB access uses SELECT-only queries and environment-based credentials.
- Reports identify keys and mismatched columns without copying business values.
- Binary keys are represented by a SHA-256 fingerprint and length instead of raw data.
- Reports, local databases, exports, passwords, and connection strings are excluded from Git.

## Technical areas

Python 3.11 · SQLite · MySQL/MariaDB · SQL reconciliation · CLI design · pytest · synthetic
test data · privacy-aware reporting

## What this demonstrates

The project demonstrates a valuable engineering habit: do not call a migration complete merely
because it ran. Verify the result, report differences safely, and preserve a clear rollback and
data-protection boundary.
