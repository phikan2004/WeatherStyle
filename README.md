# WeatherStyle 🌤️

A personalized weather advisory system that recommends what to wear based on real-time weather — delivered via **iMessage using OpenClaw** (recommended) or SMS via the legacy Flask app.

---

## OpenClaw Setup (Recommended — iMessage on your phone)

Interact with the weather outfit advisor directly from iMessage. No web form, no Twilio needed.

### 1. Install OpenClaw

```bash
npm install -g openclaw@latest
openclaw onboard --install-daemon
```

During onboarding, connect iMessage as your channel (via BlueBubbles or the legacy iMessage option).

### 2. Install the skill

```bash
cp -r skills/weather-outfit ~/.openclaw/workspace/skills/
```

### 3. Use it from your phone

Send a message to your OpenClaw assistant via iMessage:

> "What should I wear today in New York?"

The assistant fetches live weather (no API key needed) and replies with clothing recommendations.

---

## Legacy Flask App (SMS via Twilio)

✨ **AI-Powered Recommendations** – Uses OpenAI to generate clothing suggestions based on current weather

📍 **Location-Based Weather** – Fetches real-time data from OpenWeatherMap

📱 **SMS Delivery** – Sends recommendations to your phone via Twilio

### Setup

**Prerequisites:** Python 3.7+, API keys for OpenWeatherMap, OpenAI, and Twilio.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/phikan2004/WeatherStyle.git
   cd WeatherStyle
   ```

2. **Install dependencies:**
   ```bash
   pip install flask requests openai twilio
   ```

3. **Set environment variables:**
   ```bash
   export OPENAI_API_KEY=your_key
   export OPENWEATHERMAP_API_KEY=your_key
   export TWILIO_ACCOUNT_SID=your_sid
   export TWILIO_AUTH_TOKEN=your_token
   export TWILIO_PHONE_NUMBER=your_number
   ```

4. **Run the server:**
   ```bash
   python backend.py
   ```

5. Open your browser at `http://localhost:5000`

### API Endpoint

**POST `/submit`**

```json
{
  "phone": "+1234567890",
  "location": "New York, USA",
  "wake_up_time": "06:30"
}
```

---

## Project Structure

```
WeatherStyle/
├── skills/
│   └── weather-outfit/
│       └── SKILL.md       # OpenClaw iMessage skill
├── backend.py             # Legacy Flask server
├── frontend.html          # Legacy web interface
└── README.md
```

## License

MIT License. See [LICENSE](LICENSE) for details.
