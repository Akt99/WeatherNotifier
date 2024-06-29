import requests as req
from twilio.rest import Client
OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "generate your own api key by signing up for free"
account_sid = "generate your own account sid"
auth_token = "your auth_token  "
weather_params = {
    "lat": 19.075983,  #mumbai
    "lon": 72.877655,
    "appid": api_key,
    "cnt": 4,
}
response = req.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
 \
        .create(

        body="It is going to rain today, please stay safe! your well wisher @akt, take care",
        from_="whatsapp:YOUR_GENERATED_NUMBER",
        to="whatsapp:RECIPIENT_NUMBER"

    )
print(message.status)
