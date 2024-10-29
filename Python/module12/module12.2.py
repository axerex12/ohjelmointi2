import requests
import json

def ctof(lämpöf):


API_Key = "d43fb48d7c36a2d1404e5fa75121fb5d"
#city_name = input("Anna kaupungin nimi englanniksi: ")
city_name = "London"

vastaus = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}").json()
print(vastaus)
sää = vastaus['weather']
säää = sää[0]
lämptila = vastaus["main"]
lämptilaf = lämptila["temp"]


print(säää["description"])
print(lämptilac)
