import requests
import json
from dadata import Dadata
from dotenv import load_dotenv
import os
import string
import re
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Border, Side
# Загружаем переменные из файла .env
load_dotenv()
# Пример использования переменных
token = os.getenv("TOKEN")
secret = os.getenv("SECRET")
ya_apikey = os.getenv("YA_APIKEY")

def ya_maps_proccess(req):
    r = requests.get(f'https://suggest-maps.yandex.ru/v1/suggest?apikey={ya_apikey}&text={req}&print_address=1')
    final_result = ''
    if hasattr(json.loads(r.text), 'results') or 'results' in json.loads(r.text):
        final_result = json.loads(r.text)["results"][0]['address']['formatted_address']
    return final_result

# for x in range(50):
#     print(ya_maps_proccess("989uj9u"))