from flask import Flask, request, jsonify
import requests
import openai
import os
from twilio.rest import Client

app = Flask(__name__)

# Load API keys from environment variables
openai.api_key = os.environ.get("OPENAI_API_KEY")
openweathermap_api_key = os.environ.get("OPENWEATHERMAP_API_KEY")

# Twilio API credentials
twilio_account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
twilio_auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
twilio_phone_number = os.environ.get("TWILIO_PHONE_NUMBER")

@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.get_json()
    phone = data.get("phone")
    location = data.get("location")
    wake_up_time = data.get("wake_up_time")

    # Fetch weather data
    weather_data = get_weather(openweathermap_api_key, location)

    # Analyze weather data
    clothing_recommendations = analyze_weather(weather_data)

    # Send SMS message with clothing recommendations
    send_sms_twilio(phone, clothing_recommendations)

    response_data = {
        "message": "Data received successfully. Clothing recommendations will be sent to your phone daily."
    }
    return jsonify(response_data)

def get_weather(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def analyze_weather(weather_data):
    temperature = weather_data['main']['temp']
    weather_description = weather_data['weather'][0]['description']

    # Send the weather data to OpenAI for analysis
    prompt = f"Provide clothing recommendations for weather conditions: Temperature {temperature}°C and {weather_description}."
    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150
    )

    return response.choices[0].message.content

def send_sms_twilio(to_number, message):
    client = Client(twilio_account_sid, twilio_auth_token)
    client.messages.create(
        to=to_number,
        from_=twilio_phone_number,
        body=message
    )

if __name__ == '__main__':
    app.run(debug=True)
