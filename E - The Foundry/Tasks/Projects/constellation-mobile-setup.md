---
tags:
  - task
  - project
  - constellation
title: "Constellation Mobile - Claude Code Setup"
status: open
priority: normal
due: "2026-03-15"
owner: David
projects:
  - "[[Constellation Mobile]]"
---

# Constellation Mobile - Claude Code Setup

Access Claude Code from iPhone to work with Obsidian vault using old Mac/PC as always-on home server.

## Setup Steps

- [x] **Prepare old Mac/PC as home server**
  - Choose which old device to use (Mac or PC)
  - Ensure device can stay powered on 24/7
  - Position in good location (good wifi, ventilation)
  - Set up power saving settings (no sleep mode)

- [ ] **Install Node.js and Claude Code**
  - Download and install Node.js (latest LTS version)
  - Install Claude Code CLI: `npm install -g @anthropic-ai/claude-code`
  - Verify installation: `claude-code --version`
  - Authenticate Claude Code with API key

- [ ] **Install and Configure Tailscale**
  - Download Tailscale for server OS
  - Install Tailscale on server
  - Sign in and connect to network
  - Install Tailscale on iPhone
  - Verify devices see each other on Tailscale network

- [ ] **Enable SSH on Server**
  - Enable SSH service on server
  - Test SSH connection from local network
  - Create SSH key pair for passwordless auth
  - Configure SSH config file

- [ ] **Set up SSH Client on iPhone**
  - Install Termius app (recommended SSH client)
  - Add server connection using Tailscale IP
  - Test connection from iPhone over Tailscale
  - Save connection for quick access

- [ ] **Sync Obsidian Vault**
  - If Mac server: Already synced via iCloud
  - If PC server: Set up git sync or Dropbox
  - Verify vault accessible from server
  - Create shell alias for vault path
  - Test Claude Code commands on vault

**Why matters:** Mobile access to Claude Code enables working with Obsidian vault from anywhere. Home server approach is free (using existing hardware) and provides secure remote access via Tailscale VPN.

**Done when:** Can SSH from iPhone to home server via Tailscale, run Claude Code commands on Obsidian vault, and edit notes remotely.

**Related:** [[Constellation Mobile]] • [[Claude Code Mobile Setup]]

---

## Technical Architecture

**Components:**
1. **Home Server** - Old Mac or PC (always-on)
2. **Tailscale** - Secure VPN for remote access
3. **SSH** - Secure shell access to server
4. **Termius** - iPhone SSH client app
5. **Claude Code** - AI assistant for vault work
6. **Obsidian Vault** - Synced to server (iCloud or git)

**Flow:**
iPhone (Termius) → Tailscale VPN → Home Server (SSH) → Claude Code → Obsidian Vault

---

## Alternative Hardware Options

If old Mac/PC not suitable:

**Mac Mini** (used) - $200-300
- Small, quiet, efficient
- macOS with iCloud sync built-in

**Raspberry Pi 5** - ~$80
- Tiny, low power
- Linux-based, requires setup

**Small VPS** - $5-10/month
- Cloud-based, always available
- No hardware maintenance

Current plan uses existing hardware (free option).

---

## Verification Checklist

After setup complete:

- [ ] Can access server via Tailscale from iPhone (anywhere)
- [ ] Can SSH into server from Termius app
- [ ] Claude Code installed and authenticated on server
- [ ] Obsidian vault accessible from server terminal
- [ ] Can run basic Claude Code commands on vault
- [ ] Termius connection saved for quick access
- [ ] Server stays powered on and connected

---

## Timeline Flexibility

**Target:** March 15, 2026

**Reality:** This is a "nice to have" project with flexible timeline. With baby arriving and career transition underway, this may shift to April-May or later. No urgency - prioritize Batches 1-3 first.

---

## Resources

- Setup guide: [[Claude Code Mobile Setup]] (detailed step-by-step)
- Tailscale docs: https://tailscale.com/kb/
- Termius app: iOS App Store
- Claude Code docs: https://docs.anthropic.com/claude-code
