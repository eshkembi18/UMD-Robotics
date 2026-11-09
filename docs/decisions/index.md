# Engineering Decision Log

<p class="gr-meta">Maintainer: whole team</p>

Short records of the choices we made, so the next team doesn't have to redo the same debates. New one:

```bash
python scripts/new_entry.py adr 004 "decision title"
```

Format: [ADR template](../page-templates/adr.md). If a decision changes later, don't edit the old record. Write a new one and mark the old one *Superseded*.

| ID | Decision | Date | Status |
|---|---|---|---|
| [ADR-001](adr-001-xlerobot-build-guide.md) | Use XLeRobot docs as the main build guide | [TEAM VERIFICATION REQUIRED] | Accepted |
| [ADR-002](adr-002-ncsa-delta-training.md) | Train on NCSA Delta | [TEAM VERIFICATION REQUIRED] | Accepted |
| [ADR-003](adr-003-mkdocs-docs.md) | MkDocs Material for project documentation | 2026-11-07 | Accepted |

## Ideas for future ADRs

- Which policy / pretrained model to use
- Camera choice and placement
- Environment manager (conda vs uv vs venv)
- Where datasets and checkpoints are stored
