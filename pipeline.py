from extract import extract_weather
from transform import transform_weather
from load import load_weather


data = extract_weather()

df = transform_weather(data)

print("Data to load:")
print(df)

load_weather(df)

print("Data loaded successfully!")