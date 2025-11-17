# WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

from langchain.tools import tool
import requests
import json

WEATHER_API_KEY="f1e4f948674b87a15dadab6f800f1552"

@tool
def get_weather(Location: str):
    """Get the current weather for a given location"""
    url = f"http://api.weatherstack.com/current?access_key={WEATHER_API_KEY}&query={Location}"
    response = requests.get(url)
    data = response.json()
    temperature = data['current']['temperature']
    weather_descriptions = data['current']['weather_descriptions'][0]
    return f"The current temperature in {Location} is {temperature}°C with {weather_descriptions}."

@tool
def get_location(IP: str):
    """Get current location from IP"""
    url = f"https://speed.cloudflare.com/meta"
    response = requests.get(url)
    data = response.json()
    Location = data['city']
    # rates = data['pairs']['rate']
    # exchange = data['rate']
    return f"Your computer location is {Location}"

