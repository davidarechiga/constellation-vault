# Claude Code Mobile Setup

> Access Claude Code from your iPhone to work with your Obsidian vault, using your old Mac/PC as an always-on home server.
> **Task Syntax:** See [[Task Syntax Quick Reference]] for formatting

---

## Why This Approach

- **Bluehost shared hosting** won't work - no root access to install Claude Code
- **Home server** is free (you already have the hardware) and gives full control
- **Tailscale** provides secure access from anywhere without complex networking

---

## Setup Steps

### 1. Prepare the Old Mac/PC


### 2. Install Claude Code on the Server

```bash
# Install Node.js (if not installed)
# On Mac:
brew install node

# Install Claude Code
npm install -g @anthropic-ai/claude-code

# Authenticate
claude
```

### 3. Install Tailscale (Secure Remote Access)


This gives you a secure connection from anywhere - no port forwarding or VPN complexity.

### 4. Enable SSH on the Server

**On Mac:**
- System Settings → General → Sharing → Remote Login → Enable

**On Windows/Linux:**
- Enable OpenSSH server

### 5. Set Up iPhone

  - Host: `[server-name]` (Tailscale hostname, e.g., `davids-mac`)
  - Username: your Mac username
  - Authentication: password or SSH key

### 6. Sync the Obsidian Vault

**If server is a Mac:**
- Vault already syncs via iCloud - just open the same path
- `/Users/[username]/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain (iCloud)`

**If server is a PC:**
- Use git to clone the vault from a remote (GitHub, etc.)
- Or set up Syncthing/Dropbox to sync

---

## Usage Workflow

1. Open Tailscale on iPhone (connects automatically)
2. Open Termius → Connect to your server
3. Navigate to vault: `cd "~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain (iCloud)"`
4. Run: `claude`
5. Work with your notes using Claude Code

**Tip:** Create a shell alias for the long path:

```bash
echo 'alias vault="cd ~/Library/Mobile\\ Documents/iCloud~md~obsidian/Documents/Second\\ Brain\\ \\(iCloud\\)"' >> ~/.zshrc
```

---

## Alternative: Check Bluehost Hosting Type

To verify your Bluehost plan:

1. Log into Bluehost dashboard
2. Look for "VPS" or "Dedicated" in your plan name
3. If you have SSH access with root/sudo, it might work

Most Bluehost users have shared hosting which won't support Claude Code.

---

## Verification Checklist


---

## Hardware Alternatives

If the old Mac/PC is too power-hungry or noisy, consider:

- **Mac Mini** (used ~$200-300) - quiet, low power, ideal for this
- **Raspberry Pi 5** (~$80) - very low power, runs Claude Code
- **Small VPS** (~$5-10/month) - DigitalOcean, Linode, Hetzner
