import openmeteo_requests
import math
import requests_cache
import pandas as pd
import numpy as np
from retry_requests import retry



def pullWeatherData(lat, long):
	'''
	Pulls Weather Data fir the current day using the Open-Meteo API. 
	Returns a Dictionary containing Weather data.
	'''

    # Setup the Open-Meteo API client with cache and retry on error
	cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
	retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
	openmeteo = openmeteo_requests.Client(session = retry_session)

	# Make sure all required weather variables are listed here
	# The order of variables in hourly or daily is important to assign them correctly below
	url = "https://api.open-meteo.com/v1/forecast"
	params = {
		"latitude": lat,
		"longitude": long, 
		"daily": ["temperature_2m_max", "temperature_2m_min", "sunrise", "sunset", "rain_sum", "showers_sum"],
		"temperature_unit": "fahrenheit",
    		"precipitation_unit": "inch",
		"forecast_days": 1
}
	# Set Responses
	responses = openmeteo.weather_api(url, params=params)

	# Process first location. Add a for-loop for multiple locations or weather models
	response = responses[0]
	"""
print(f"Coordinates {response.Latitude()}N {response.Longitude()}E")
print(f"Elevation {response.Elevation()} m asl")
print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")
"""

	# Process daily data. The order of variables needs to be the same as requested.
	daily = response.Daily()
	weatherDict = {
		"Today's High" : int(daily.Variables(0).ValuesAsNumpy()[0]),
		"Today's Low" : int(daily.Variables(1).ValuesAsNumpy()[0]),
		"Today's Sunrise" : daily.Variables(2).ValuesAsNumpy(),
		"Today's Sunset" : daily.Variables(3).ValuesAsNumpy(),
		"Today's Rainsum" : daily.Variables(4).ValuesAsNumpy()[0],
		"Today's Showers" : daily.Variables(5).ValuesAsNumpy()[0]
	}

	"""
	daily_data = {"date": pd.date_range(
		start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
		end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
		freq = pd.Timedelta(seconds = daily.Interval()),
		inclusive = "left"
	)}


	daily_data["temperature_2m_max"] = daily_temperature_2m_max
	daily_data["temperature_2m_min"] = daily_temperature_2m_min
	daily_data["sunrise"] = daily_sunrise
	daily_data["sunset"] = daily_sunset
	daily_data["rain_sum"] = daily_rain_sum
	daily_data["showers_sum"] = daily_showers_sum
	"""
	return weatherDict


