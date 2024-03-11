#pip install requests in cmd line


import requests
import json

def get_weather(city_name):
    api_key = "dbe55cc00ca52d77f52a8debaf07c800"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    complete_url = base_url + "?q=" + city_name + "&appid=" + api_key + "&units=metric"
    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()
        main = data["main"]
        temperature = main["temp"]
        humidity = main["humidity"]
        weather_desc = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]
        print("Temperature : " + str(temperature) + " °C" +
              "\nHumidity : " + str(humidity) + " %" +
              "\nDescription : " + str(weather_desc) +
              "\nWind Speed : " + str(wind_speed) + " m/s")
    else:
        print("Error:", response.status_code, response.text)

city_name = input("Enter city name : ")
get_weather(city_name)