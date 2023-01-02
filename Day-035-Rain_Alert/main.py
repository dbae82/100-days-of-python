import requests
from twilio.rest import Client
import os

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWM_API_KEY")
account_sid = "ACc9f9326e47cac10d887a53ec0504b6a9"
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

weather_params = {
    "lat": 29.760427,
    "lon": -95.369804,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
data = response.json()
data_slice = data["hourly"][:12]

will_rain = False

for hour_data in data_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_='+12525571469',
        to='YOUR PHONE NUMBER'
    )
    print(message.status)
