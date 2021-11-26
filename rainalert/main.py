import requests
from twilio.rest import Client
import os
from twilio.http.http_client import TwilioHttpClient

url = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "441642d586db0aae92e3476149c8900e"
account_sid = "AC8638efcb254fc0e1967ccc5f1cb0173c"
auth_token = "95b9333e621909e7e1749b055990d162"


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
        from_="+15203418419",
        to="+6281294553934"
    )
print(message.status)





