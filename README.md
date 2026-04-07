---
title: Email Triage Environment
emoji: 📧
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
pinned: false
---

# Email Triage Environment

An OpenEnv environment for intelligent email triage.

**Author:** Adwait Mulay | **HF Username:** Adwait07

## Tasks
| Task | Difficulty |
|------|-----------|
| spam_detection | Easy |
| department_routing | Medium |
| full_triage | Hard |

## Run locally
```bash
pip install openenv-core
uvicorn server.app:app --host 0.0.0.0 --port 8000
```