# WakeMeUpWithWeather

This is a small personal project that uses the Open Meteo Weather API to fetch weather forecast data and send it via gmail SMTP to SMS to yourself or others. The project allows users to manage a list of subscribers through an csv file.

## Features

    - Fetches weather forecast data from the Open Meteo Weather API. (No API key required for accessing the weather data.)
    - Sends weather forecast information via SMTP to SMS.
    - Reads a list of 'subscribers' via a csvfile.
    - Can be scheduled to run at a specific time each day.
    

## Requirements

    Python 3.x

The detailed list of requirements can be found in the requirements.txt file.
Setup


Update the gmail SMTP configuration in a .env file located in the project directory, setting the following information:

    SMTPAUTHPASS="YOUR-GMAIL-AUTHENTICATION"
    SMTPEMAIL="YOUR-EMAIL@GMAIL.COM"
    SUBSCRIBERS="PATH-TO-SUBSCRIBER-CSV"

## Create a subscribers file:

Create a file like the one below (a header is required, but the data in it is currently not used) 
Each line in the file should contain the following information for each subscriber: phone number, carrier, latitude, longitude, and location name.

Example csv:

    phone,carrier,lat,long,location name
    1234567890,tmobile,37.7749,-122.4194,San Francisco
    0987654321,verizon,34.0522,-118.2437,Los Angeles

## Usage

Run the script manually:

    python3 .\WakeMeUpWithWeather.py

## Acknowledgements

Open Meteo Weather API for providing the weather forecast data : https://open-meteo.com/en/docs
