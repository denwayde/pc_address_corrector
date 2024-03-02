import requests
import json
from dadata import Dadata
from dotenv import load_dotenv
import os
# Загружаем переменные из файла .env
load_dotenv()
# Пример использования переменных
token = os.getenv("TOKEN")
secret = os.getenv("SECRET")
ya_apikey = os.getenv("YA_APIKEY")
dadata = Dadata(token, secret)


n="Кононенко Виталий"#ETO NUJNO PROVERYAT NA NALICHIE CIFR
n1 = "7 960 391-52-45 - Исходящий звонок" #result['result'] --- None
s13 = "г.Уфа Менделеева ул. 128/1, гараж. Бокс 26"


r = requests.get(f'https://suggest-maps.yandex.ru/v1/suggest?apikey={ya_apikey}&text={s13}&print_address=1')
# print(json.loads(r.text)["results"])
# if hasattr(json.loads(r.text), "results"):
#     print('has')
# else:
#     print('dont')
#print(json.loads(r.text)["results"][0])

result = dadata.suggest("address", s13)
print(result[0])

