from flask import Flask
import requests
import json


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'XXXXXXxxxxx'


def getWeatherData():
    api_key = 'b50ee755aaca2543ce4ead37008f18d6'
    city_id = '4164138'
    payload = {'id': city_id, 'APPID': api_key}

    weather = requests.get(
        'http://api.openweathermap.org/data/2.5/weather', params=payload)

    print(weather.raise_for_status())
    print(weather.status_code)
    weatherData = weather.json()
    print(weatherData['weather'])


if __name__ == '__main__':
    app.run()

#  "id": 4164138,
#     "name": "Miami",
#     "country": "US",
#     "coord": {
#       "lon": -80.193657,
#       "lat": 25.774269
