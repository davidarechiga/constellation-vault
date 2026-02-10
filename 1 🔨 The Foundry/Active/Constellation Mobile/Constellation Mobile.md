---
tags: [project]
title: "Constellation Mobile"
status: active
category: personal
priority: medium
owner: David
start-date: 2026-01-15
last-updated: 2026-02-08
progress: 10
deadline: 2026-04-15
current-focus: Server setup and VPN configuration
next-action: Complete Tailscale VPN setup and SSH configuration
time-estimate: 4-6 weeks
deliverables:
  - Home server accessible via iPhone
  - Tailscale VPN configured
  - SSH access from Termius app
  - Vault syncing on mobile
  - Claude Code integration via home server
collaborators: [David]
related-files: ["[[Career Transition 2026]]", "[[2026 S.M.A.R.T. Goals]]"]
---

# Constellation Mobile

> **Goal:** Access Claude Code and your Obsidian vault from iPhone via secure home server connection
> **Context:** Portfolio project showcasing infrastructure + mobile development skills for Creative Technologist role

---

## 📊 Project Overview

**Status:** Active - Setup Phase
**Priority:** Medium (portfolio project for career transition)
**Completion:** ~10%
**Timeline:** January - April 2026
**Target Completion:** March 15, 2026 (flexible, may shift to April-May with baby arrival)

Access your Constellation vault and Claude Code capabilities from iPhone through a home server + VPN setup. This project serves dual purposes:
1. **Practical:** Mobile access to your knowledge management system while traveling or away from desk
2. **Professional:** Demonstrates infrastructure knowledge, mobile development, and creative problem-solving for Creative Technologist interviews

---

## 🎯 Project Goals

1. **Remote Access Setup**
   - Secure connection from iPhone to home server
   - No cloud dependencies (privacy-first approach)
   - Works from anywhere (cellular, WiFi, traveling)

2. **Development Showcase**
   - Document setup process for portfolio
   - Demonstrate infrastructure skills (VPN, SSH, networking)
   - Show initiative in solving own technical challenges

3. **Functional Integration**
   - Run Claude Code from mobile environment
   - Access vault files seamlessly
   - Mobile-optimized interface (Termius app)

---

## 🔧 Technical Architecture

### Infrastructure Stack
- **VPN:** Tailscale (wireguard-based, user-friendly)
- **SSH:** Standard SSH protocol
- **Terminal App:** Termius (iOS SSH client)
- **Server:** Home Linux/Mac server (always-on)
- **Sync:** iCloud sync for vault, alternative: Dropbox/Git

### Setup Phases

#### Phase 1: Tailscale VPN ✓ (Planned)
- [ ] Create Tailscale account
- [ ] Install Tailscale on home server
- [ ] Configure auth keys
- [ ] Test iPad/iPhone connection

#### Phase 2: SSH Configuration ✓ (Planned)
- [ ] Set up SSH keys (no password auth)
- [ ] Configure SSH server on home machine
- [ ] Create mobile user account
- [ ] Test SSH access from Termius

#### Phase 3: Claude Code Integration 🔄 (Current)
- [ ] Install Claude Code CLI on home server
- [ ] Configure ~/.claude directory
- [ ] Set up vault access via mobile terminal
- [ ] Test Claude Code commands from iPhone

#### Phase 4: Vault Sync
- [ ] Configure iCloud/Dropbox sync on server
- [ ] Enable sync on mobile device
- [ ] Test bidirectional file updates
- [ ] Document sync workflow

#### Phase 5: Optimization & Documentation
- [ ] Create setup guide (for portfolio)
- [ ] Document troubleshooting steps
- [ ] Record process video (optional)
- [ ] Create case study for interviews

---

## 📱 Mobile UX Design

### Termius App Interface
- **Quick Access Buttons:** Vault sync, Claude Code shortcuts
- **Command Shortcuts:** Common Claude Code operations
- **Status Indicators:** Sync status, connection health

### Workflow Examples
1. **Morning:** Connect via VPN → Check daily note in mobile Termius
2. **During Day:** Quick task update via mobile terminal
3. **On Go:** Full vault access without carrying laptop

---

## 🔐 Security Considerations

- **VPN:** Tailscale handles encryption (WireGuard protocol)
- **SSH Keys:** No password authentication (key-based only)
- **Network:** Home server never exposed directly to internet
- **Backups:** Regular vault backups before any configuration changes

---

## 📊 Timeline & Milestones

| Phase | Target Date | Milestone | Status |
|-------|-------------|-----------|--------|
| Tailscale VPN | Feb 20, 2026 | Remote access working | Planned |
| SSH Config | Feb 28, 2026 | iPhone terminal access | Planned |
| Claude Integration | Mar 15, 2026 | Mobile Claude Code working | Planned |
| Vault Sync | Mar 31, 2026 | Full bidirectional sync | Planned |
| Documentation | Apr 15, 2026 | Case study complete | Planned |

---

## 🎓 Learning Outcomes

**Infrastructure Knowledge:**
- VPN setup and configuration (Tailscale/WireGuard)
- SSH key management and security
- Home server administration
- Network troubleshooting

**Mobile Development:**
- iOS terminal apps and their capabilities
- Mobile-optimized command-line workflows
- SSH client apps and configurations

**Documentation:**
- Creating technical guides for non-technical users
- Building case studies for interviews
- Demonstrating problem-solving process

---

## 🤝 Integration with Career Transition

**Why This Matters for Interviews:**
1. **Shows Initiative:** Solved own technical problems
2. **Demonstrates Skills:** Infrastructure + mobile + documentation
3. **Creative Problem-Solving:** Found novel way to access dev tools on mobile
4. **Real-World Value:** Built something genuinely useful
5. **Case Study Material:** Great portfolio project to discuss

**Interview Talking Points:**
- "I needed mobile access to my development environment, so I built..."
- "This project taught me about VPN setup, SSH security, and mobile workflows"
- "It shows I can solve complex technical problems independently"

---

## 📚 Resources & Documentation

### VPN & SSH
- Tailscale docs: https://tailscale.com/kb/
- SSH best practices: https://man.openbsd.org/ssh_config
- WireGuard protocol overview: https://www.wireguard.com/

### Mobile Terminal
- Termius iOS app documentation
- SSH on iOS workflows

### Portfolio Documentation
- Setup guide (to write)
- Process video (to record)
- Case study (to create)

---

## 🔗 Related Projects

- [[Career Transition 2026]] — This project enhances portfolio for interviews
- [[2026 S.M.A.R.T. Goals]] — Supports goal of "expand technical skills"
- [[Frameloop]] — Another portfolio project demonstrating creative tech
- [[Constellation Mobile]] — The actual vault application

---

## 📝 Development Notes

**Why Home Server Approach:**
- Privacy: No data stored on cloud services
- Cost: Free (uses existing home infrastructure)
- Learning: Deep understanding of networking and systems
- Showcase: Impressive to discuss in interviews

**Considerations:**
- Home server must stay on (or wake-on-LAN)
- Network stability required
- Backup procedures essential
- Documentation is the real deliverable

**Post-MVP:**
- Could build custom iOS app (SwiftUI frontend)
- Could add git integration for vault management
- Could create automation scripts
- Could extend to iPad for full editor experience

---

*Last Updated: February 8, 2026*
*Constellation Mobile Setup Project v1.0*
