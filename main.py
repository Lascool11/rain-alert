from venv import create
import os

import requests
from twilio.rest import Client

MY_LAT = 43.733334
MY_LNG = 7.416667

account_sid = "AC24982035d0ab691e6575ccae4e6995cf"
auth_token = os.environ.get("AUTH_TOKEN")

"""
Until now, we have seen free APIs, we could access all parts of it without any sort of payment. This is because the data
that is contained in those APIs is very simple. On the other hand, there are other types of data that are very valuable,
like weather data, because it takes a lot of energy and time for a company to collect all this data. For this reason,
some of these APIs can have a paid tier. Most of the time, these companies also have a free tier, and to prevent big
companies to claim those free tiers, they use something called an 'API Key' so that the API provider can track how much 
you are using their APIs and to authorize your access or not depending on your membership. 
"""

parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": os.environ.get("OWM_API_KEY"),
    "units": "metric",
    "cnt": 4
}

response = requests.get(url = "https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

is_going_to_rain = False

for element in weather_data["list"]:
    if int(element["weather"][0]["id"]) < 700:
        is_going_to_rain = True

if is_going_to_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today! Remember to bring an ☔️",
        from_="+16416663460",
        to="+33640610093",
    )

"""
Environment variables are external key–value settings stored by the operating system. They are useful for keeping 
sensitive or configurable data (like API keys, passwords, or environment-specific settings) outside the source code, 
making applications more secure, flexible, and easier to deploy across different environments. We can create an 
environment variable by typing 'export' and then the name of the variable followed by an equal sign, and the value of 
that variable on the python console. For example: 'export OWM_API_KEY=6f1e793535d02bd367ba67ce18296bfe'. Once we have
created it our environment variable, we can tap into it in any of the code that we run from this particular environment.
To do that, we have to import and use the 'os' module, and then use the method: 'os.environ.get("OWM_API_KEY")'. 
"""

