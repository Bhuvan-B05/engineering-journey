import requests

print("Starting request...")

url = "https://api.open-meteo.com/v1/forecast?latitude=17.6868&longitude=83.2185&current_weather=true"

response = requests.get(url, timeout=10)

print("Request completed")

print(response.status_code)
data=response.json()
weather=data["current_weather"]
print("Temperature: ",weather["temperature"],"Celsius")
print("Wind speed: ",weather["windspeed"],"km/h")
print("TIme: ",weather["time"])
