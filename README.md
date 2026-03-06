# WeatherStyle 🌤️

Get clothing recommendations based on current weather, delivered to your phone via iMessage using [OpenClaw](https://github.com/openclaw/openclaw).

## How It Works

1. OpenClaw runs in the background on your Mac
2. Text your own Apple ID or phone number from your iPhone
3. The AI fetches live weather via [wttr.in](https://wttr.in) and replies with clothing recommendations

---

## Setup Guide

### Prerequisites

- macOS with Messages.app signed in to your Apple ID
- Node.js v22+
- Homebrew

### 1. Upgrade Node.js to v22

OpenClaw requires Node.js v22 or higher.

```bash
brew install node@22
brew link --overwrite node@22
export PATH="/opt/homebrew/opt/node@22/bin:$PATH"
node --version  # should show v22.x.x
```

### 2. Install OpenClaw

```bash
npm install -g openclaw@latest
openclaw onboard --install-daemon
```

During onboarding:
- **AI model:** Choose Anthropic and enter your API key from [console.anthropic.com](https://console.anthropic.com/settings/keys)
- **Channel:** Choose iMessage (imsg)
- **imsg CLI path:** Press Enter to accept the default (`imsg`)
- **Skills:** Skip for now
- **Hatch:** Choose "Hatch in TUI"

> ⚠️ Make sure your Anthropic account has credits at [console.anthropic.com/settings/billing](https://console.anthropic.com/settings/billing). A Claude Pro subscription does NOT include API credits — they are purchased separately.

### 3. Install imsg

```bash
brew install steipete/tap/imsg
```

### 4. Grant Full Disk Access to VS Code (or your terminal)

imsg needs Full Disk Access to read the Messages database.

1. Go to **System Settings → Privacy & Security → Full Disk Access**
2. Click **+** and add your terminal app (e.g. Visual Studio Code)
3. Toggle it **on**
4. Quit and reopen your terminal completely

### 5. Install the weather-outfit skill

```bash
cp -r skills/weather-outfit ~/.openclaw/workspace/skills/
```

### 6. Enable full tool access

This allows the agent to run `curl` to fetch live weather:

```bash
openclaw config set tools.profile full
```

### 7. Start the gateway

Run this in a terminal and **keep it open**:

```bash
openclaw gateway
```

> ⚠️ Always run the gateway from the terminal that has Full Disk Access (e.g. VS Code terminal). If you run it as a background daemon via `launchctl`, it won't inherit Full Disk Access and iMessage won't work.

### 8. Pair your iPhone

Text your own phone number from your iPhone with any message. OpenClaw will reply with a pairing code, e.g.:

```
OpenClaw: access not configured.
Your iMessage sender id: +1xxxxxxxxxx
Pairing code: XXXXXXXX
Ask the bot owner to approve with:
openclaw pairing approve imessage XXXXXXXX
```

In a new terminal tab, run:

```bash
openclaw pairing approve imessage XXXXXXXX
```

### 9. Test it

From your iPhone, text yourself:

> "What should I wear today in New York?"

You'll get a live weather check and clothing recommendations back via iMessage.

---

## Usage

Just text naturally from your iPhone:

- "What should I wear today in London?"
- "Do I need a jacket in Chicago?"
- "Outfit for rainy weather in Seattle?"

---

## Restarting after a Mac reboot

Each time you restart your Mac, run this from VS Code terminal:

```bash
openclaw gateway
```

Keep the terminal open while using the app.

---

## Project Structure

```
WeatherStyle/
├── skills/
│   └── weather-outfit/
│       └── SKILL.md    # OpenClaw skill definition
└── README.md
```
