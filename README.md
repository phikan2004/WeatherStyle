# WeatherStyle 🌤️

A personalized daily weather advisory system that sends clothing recommendations via SMS based on real-time weather conditions. Never let unpredictable weather ruin your day—WeatherStyle helps you dress appropriately with AI-powered recommendations delivered straight to your phone.

## Features

✨ **AI-Powered Recommendations** – Uses OpenAI's language models to generate personalized clothing suggestions based on current weather conditions

📍 **Location-Based Weather Data** – Fetches real-time weather information from OpenWeatherMap API for your specified location

📱 **SMS Delivery** – Sends recommendations directly to your phone using Twilio, ensuring you receive updates at the start of your day

⏰ **Customizable Scheduling** – Set your preferred wake-up time to receive recommendations when you need them most

🎯 **Simple Setup** – Easy-to-use web interface for entering your information and preferences

## How It Works

1. **User Input** – Enter your phone number, location, and preferred wake-up time via the web interface
2. **Weather Retrieval** – The system fetches current weather data (temperature, conditions) for your location
3. **AI Analysis** – OpenAI analyzes the weather conditions and generates clothing recommendations
4. **SMS Notification** – Recommendations are sent to your phone via Twilio
5. **Outfit Optimization** – Get dressed with confidence based on intelligent, weather-aware suggestions

## Tech Stack

- **Backend:** Python with Flask (lightweight web framework)
- **Frontend:** HTML with vanilla JavaScript
- **Weather API:** OpenWeatherMap API
- **AI/LLM:** OpenAI API (text-davinci-002)
- **SMS Service:** Twilio

## Project Structure

```
WeatherStyle/
├── backend.py          # Flask server, API integrations, and weather analysis
├── frontend.html       # User-facing web interface
├── README.md          # This file
└── LICENSE            # Project license
```

## Installation & Setup

### Prerequisites
- Python 3.7+
- Valid API keys for:
  - [OpenWeatherMap](https://openweathermap.org/api)
  - [OpenAI](https://platform.openai.com)
  - [Twilio](https://www.twilio.com)

### Steps

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd WeatherStyle
   ```

2. **Install dependencies:**
   ```bash
   pip install flask requests openai twilio
   ```

3. **Configure API keys:**
   Open `backend.py` and replace the placeholders with your actual API credentials:
   ```python
   openai.api_key = "YOUR_OPENAI_API_KEY"
   openweathermap_api_key = "OPENWEATHERMAP_API_KEY"
   twilio_account_sid = "YOUR_TWILIO_ACCOUNT_SID"
   twilio_auth_token = "YOUR_TWILIO_AUTH_TOKEN"
   twilio_phone_number = "YOUR_TWILIO_PHONE_NUMBER"
   ```

4. **Run the application:**
   ```bash
   python backend.py
   ```

5. **Access the interface:**
   Open your browser and navigate to `http://localhost:5000`

## Usage

1. Enter your phone number (must be in Twilio-compatible format)
2. Enter your location (city, country)
3. Set your preferred wake-up time
4. Click **Submit**
5. You'll receive a confirmation message, and clothing recommendations will be sent to your phone

## API Endpoints

### POST `/submit`
Submits user information and triggers the clothing recommendation process.

**Request Body:**
```json
{
  "phone": "+1234567890",
  "location": "New York, USA",
  "wake_up_time": "06:30"
}
```

**Response:**
```json
{
  "message": "Data received successfully. Clothing recommendations will be sent to your phone daily."
}
```

## Future Enhancements

- 📅 Scheduled SMS delivery at specified wake-up times
- 🌍 Support for multiple languages
- 👥 User accounts and preference storage
- 📊 Weather trend analysis for outfit planning
- 🌙 Seasonal and activity-specific recommendations
- 🔄 Integration with calendar for event-aware suggestions

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Notes

- Ensure your Twilio account is properly configured with sufficient credits
- OpenWeatherMap API provides free tier access for development
- OpenAI API usage incurs costs based on tokens consumed
- This project is designed for personal use; modify as needed for production deployment
