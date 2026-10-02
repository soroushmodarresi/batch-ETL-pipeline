import pandas as pd


def transform_weather(data):
    current = data["current"]

    weather = {
        "observed_at": current["time"],
        "temperature": current["temperature_2m"],
        "humidity": current["relative_humidity_2m"],
        "wind_speed": current["wind_speed_10m"],
        "city": "urmia",
        "weather_code": current["weather_code"],
    }

    df = pd.DataFrame([weather])

    df["observed_at"] = pd.to_datetime(df["observed_at"])

    return df