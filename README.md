# WeatherStyle 🌤️

Get clothing recommendations based on current weather, delivered to your phone via iMessage using [OpenClaw](https://github.com/openclaw/openclaw).

## How It Works

1. OpenClaw runs in the background on your Mac
2. Text your own Apple ID or phone number from your iPhone
3. The AI fetches live weather and replies with clothing recommendations

## Setup

### 1. Install OpenClaw

```bash
npm install -g openclaw@latest
openclaw onboard --install-daemon
```

During onboarding, select iMessage as your channel.

### 2. Install the skill

```bash
cp -r skills/weather-outfit ~/.openclaw/workspace/skills/
```

### 3. Grant Full Disk Access to your terminal

Go to **System Settings → Privacy & Security → Full Disk Access** and add your terminal app (VS Code, Terminal, etc).

### 4. Start OpenClaw

```bash
launchctl load ~/Library/LaunchAgents/ai.openclaw.gateway.plist
```

### 5. Text from your iPhone

Send an iMessage to your own phone number:

> "What should I wear today in New York?"

## Project Structure

```
WeatherStyle/
├── skills/
│   └── weather-outfit/
│       └── SKILL.md    # OpenClaw skill
└── README.md
```
