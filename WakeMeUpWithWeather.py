import datetime
from logging import getLogger
import pprint
import os
import csv
from datetime import datetime
from dotenv import load_dotenv

import WeatherData
import Notifications


def buildWeatherMessage(weatherData, location="Your"):
    # Construct Weather Message String
    messageStr = f"""\r\n\r\n{location} Weather forecast for {today}:\nToday's High is {weatherData["Today's High"]}...\nToday's Low is {weatherData["Today's Low"]}...\nThere is a {weatherData["Today's Showers"]}% chance of rain today!"""
    return messageStr
   


#Get Today's Date
today = datetime.today().strftime('%m-%d-%Y')

#Load Recepients from File
load_dotenv() # Load Environment Variables
with open(os.getenv("SUBSCRIBERS"), 'r') as subFile:
       
    
    #Create csvReader
    csvReader = csv.reader(subFile)
    header = next(csvReader)

    for row in csvReader:
        weatherData = WeatherData.pullWeatherData(float(row[2]), float(row[3]))
        Notifications.sendMessage(row[0], row[1], buildWeatherMessage(weatherData,row[4]))