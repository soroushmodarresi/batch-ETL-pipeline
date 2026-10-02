import requests


def extract_weather():
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": 37.5498,
        "longitude": 45.0786,
        "current": (
            "temperature_2m,"
            "relative_humidity_2m,"
            "wind_speed_10m,"
            "weather_code"
        ),
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json()