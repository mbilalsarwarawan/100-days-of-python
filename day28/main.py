import requests
api_key="952c54e9857c50df2ebaa7d7f8cf5c7d"
parameters={
    "appid":api_key,
    "units":"metric",
    "q":"Lahore"
}

response=requests.get("https://api.openweathermap.org/data/2.5/weather", params=parameters)
print(response.json())