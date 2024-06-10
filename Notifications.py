import smtplib
import sys
import os
from dotenv import load_dotenv


CARRIERS = {
     "att": "@mms.att.net",
    "tmobile": "@tmomail.net",
    "verizon": "@vtext.com",
    "sprint": "@messaging.sprintpcs.com"
 }



def sendMessage(phoneNumber, carrier, message):
    '''
    Send a text Message to the target phone number.
    
    params
    phoneNumber - str - Target Phone number
    carrier - str - Target Phone's Carrier
    message - str - The message to be sent
    
    '''
    
    load_dotenv()  # take environment variables from .env.

    
    target = phoneNumber + CARRIERS[carrier]
    authData = (os.getenv("SMTPEMAIL"),os.getenv("SMTPAUTHPASS"))
    
    # connect to gmail smtp server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(authData[0], authData[1])
 
    # send
    server.sendmail(authData[0], target, message)
    