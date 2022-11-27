import requests
import json
from core.settings import settings


def init(user_data):
    search_type = user_data['weather_type']
    if search_type == 'find':
        city = user_data['city']
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                           params={'q': city, 'type': 'like', 'units': 'metric', 'lang': 'ru',
                                   'APPID': settings.bots.appid})
        data = res.json()
        print(data)
        return '1234!'
