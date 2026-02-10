---
tags:
  - task
  - personal
title: "Configure SSH Access from Mobile"
status: open
priority: normal
due: "2026-02-28"
owner: David
projects:
  - "[[Constellation Mobile]]"
---

# Configure SSH Access from Mobile (Phase 2)

- [ ] Set up SSH keys (no password auth)
- [ ] Configure SSH server on home machine
- [ ] Create mobile user account
- [ ] Test SSH access from Termius app on iPhone

**Why matters**: SSH is the transport layer for all remote work. Key-based auth (no passwords) is both more secure and more convenient from mobile. Termius app provides a good mobile terminal experience.

**Done when**: Can SSH into home server from iPhone via Termius using key-based authentication.

**Related**: [[Constellation Mobile]] • [[setup-tailscale-vpn]]

---

## Security Notes
- Key-based auth only (disable password auth in sshd_config)
- Home server never directly exposed to internet (only via Tailscale)
- Separate user account for mobile access (principle of least privilege)
