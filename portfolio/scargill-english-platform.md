# Scargill English Platform

**Area:** Django web platform, scheduling, permissions, and operational delivery  
**Status:** Private repository · active development

## Purpose

Scargill English Platform is a Django-based application for online language-school workflows.
It brings together student, teacher, company, and administrative processes in one product
instead of relying on disconnected tools.

## Implemented and planned product areas

- Role-aware dashboards and account workflows.
- Invitations, permissions, and administrative access control.
- Lesson scheduling, booking flows, calendar-related functionality, and notifications.
- Course and homework workflows, certificates, support, and company-seat management.
- Payment-related integration boundaries and production-oriented deployment configuration.

## Engineering practices

- Django 5.2, PostgreSQL, Stripe integration, iCalendar, and email workflows.
- Environment-based secrets, migration discipline, and production deployment foundations with
  Ubuntu, Nginx, Gunicorn, and systemd.
- Automated testing with Django/pytest and browser-test tooling.
- Feature flags, documentation, and explicit rollout/rollback planning for higher-risk changes.

## What this demonstrates

The project demonstrates full product thinking: data models, permissions, payments, scheduling,
operations, testing, and staged delivery. It also shows why security is part of normal web
development — not a separate task left until the end.

## Public boundary

The repository is private because it contains commercial product work and operational details.
No credentials, customer information, infrastructure addresses, or production configuration are
published in this case study.
