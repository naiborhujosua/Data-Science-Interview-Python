import requests
from twilio.rest import Client
import os
from twilio.http.http_client import TwilioHttpClient

url = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "api_key"
account_sid = "account_id"
auth_token = "auth_token"


parameters ={
    "lat":-8.340539,
    "lon":115.091949,
    "appid":api_key,
    "exclude":"current,minute,daily"
}
response = requests.get(url,params=parameters)
response.raise_for_status()
data = response.json()
weather_slice = data["hourly"][:12]
will_rain =False
for hour_data in weather_slice:
    condition_code =hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain=True

if will_rain:

    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token,http_client=proxy_client)
    message = client.messages \
        .create(
        body="It is going to rain 🌧. Bring an Umbrella.",
        from_="your twilio number",
        to="your twilio verified number"
    )
print(message.status)





