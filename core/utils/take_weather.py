import requests
from core.settings import settings

ICONS = {
    '01d': '',
    '02d': ''
}


def init(user_data):
    search_type = user_data['weather_type']
    if search_type == 'find':
        city = user_data['city']
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                           params={'q': city, 'type': 'like', 'units': 'metric', 'lang': 'ru',
                                   'APPID': settings.bots.appid})
        data = res.json()
        return generate_result(data, city)
    elif search_type == 'weather':
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                           params={'lat': user_data['lat'], 'lon': user_data['lon'], 'type': 'like', 'units': 'metric',
                                   'lang': 'ru',
                                   'APPID': settings.bots.appid})
        data = res.json()
        return generate_result(data, data['list'][0]['name'])


def generate_result(data, city):
    temp = data['list'][0]['main']['temp']
    feels_like = data['list'][0]['main']['feels_like']
    pressure = data['list'][0]['main']['pressure']
    humidity = data['list'][0]['main']['humidity']
    wind_speed = data['list'][0]['wind']['speed']
    rain = 'Нет' if data['list'][0]['rain'] is None else 'Да'
    snow = 'Нет' if data['list'][0]['snow'] is None else 'Да'
    weather = data['list'][0]['weather'][0]['description']
    return f'''
<b>Актуальная погода в городе {city}</b>
Температура {temp}
ощущается как {feels_like}
Статус {weather}
Давление {pressure}, влажность {humidity}
Скорость ветра {wind_speed}
Дождь {rain}, снег {snow}
'''
