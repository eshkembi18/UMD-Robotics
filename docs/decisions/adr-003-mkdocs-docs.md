# ADR-003: MkDocs Material for Project Documentation

<p class="gr-meta">Date: 2026-11-07 · Status: Accepted · Deciders: whole team</p>

## Problem

We need documentation that outlives our team, can be edited by any student, and stays in sync with the code.

## Options considered

| Option | Pros | Cons |
|---|---|---|
| MkDocs + Material | Markdown only, built-in search, dark mode, versioned in git, free hosting on GitHub Pages | Static only |
| Docusaurus | Powerful, React-based | Needs Node/React knowledge to customize |
| Google Docs / Drive | Easy | Not versioned with the code, hard to navigate, access dies with accounts |
| Custom website | Full control | Someone has to maintain frontend code forever |

## Criteria

Editable by undergrads without frontend skills · lives in git · free · searchable · survives team turnover.

## Decision

MkDocs with Material for MkDocs, deployed to GitHub Pages by GitHub Actions.

## Tradeoffs & consequences

- No interactive features beyond what Material provides. That's acceptable for docs.
- The repo must live in a lab or department GitHub org so it survives graduation.
- The CI strict build blocks merges with broken links.
