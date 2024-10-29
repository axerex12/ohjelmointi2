import requests
import json

API_Key = "d43fb48d7c36a2d1404e5fa75121fb5d"
city_name = input("Anna kaupungin nimi englanniksi: ")


vastaus = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}&units=metric").json()
print(vastaus)
sää = vastaus['weather']
säää = sää[0]
lämptila = vastaus["main"]
lämptilac = lämptila["temp"]


print(säää["description"])
print(f"{lämptilac} celsius astetta")
