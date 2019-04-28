import requests
import json

city_name = input("Укажите имя города:")

def get_Iata_code(city_name):
    link = "https://www.travelpayouts.com/widgets_suggest_params?q=Из%20"+city_name+"%20в%20Лондон"
    data = json.loads(requests.get(link).text)
    return data["origin"]["iata"]

try:
    print(get_Iata_code(city_name))
except:
    print("Код найти не удалось, возможно Вы неверно указали имя города.")
