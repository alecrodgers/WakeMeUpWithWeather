import datetime
from logging import getLogger
import pprint
import os
from datetime import datetime
from dotenv import load_dotenv

import WeatherData
import Notifications


# Pull Weather Data for Today
weatherData = WeatherData.pullWeatherData()

#Get Today's Date
today = datetime.today().strftime('%m-%d-%Y')

# Construct Weather Message String
messageStr = f"""Here is your weather forecast for {today}:
  Today's High is {weatherData["Today's High"]}...
  Today's Low is {weatherData["Today's Low"]}...
  There is a {weatherData["Today's Showers"]}% chance of rain today!"""



# Load Environment Variables
load_dotenv()

#Send Notification
Notifications.sendMessage(os.getenv("TARGET"), os.getenv("CARRIER"), messageStr)





