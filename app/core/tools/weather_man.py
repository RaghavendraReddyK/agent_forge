import os
from langchain_community.utilities import OpenWeatherMapAPIWrapper
from langchain_core.tools import tool
from dotenv import load_dotenv
load_dotenv()

owm_api_key = os.getenv("OPENWEATHERMAP_APIKEY")
@tool
def weather_repoter():
    """
    Fetch the weather information for a given location using the OpenWeatherMap API.
    Use this tool to get current weather by providing a city name or coordinates.
    Returns a textual weather report based on the query provided.
    """
    weather = OpenWeatherMapAPIWrapper(openweathermap_api_key=owm_api_key)
    return weather.run
# tools = [weather.run]