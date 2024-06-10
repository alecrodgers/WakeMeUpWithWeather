import datetime
from logging import getLogger
import pprint
import os
import csv
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


#Load Recepients from File
subscribers = {}
load_dotenv()
with open(os.getenv("SUBSCRIBERS"), 'r') as subFile:
    
    #Create csvReader
    csvReader = csv.reader(subFile)

    for row in csvReader:
        subscribers[row[0]] = row[1]

#Send Notification
for phone, carrier in subscribers.items():
    Notifications.sendMessage(phone, carrier, messageStr)
