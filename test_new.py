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
dadata = Dadata(token, secret)

def is_punctuation(char):
    return char in string.punctuation

def cut_all_tire(text_from_exel):
    if is_punctuation(text_from_exel[0]):
        text_from_exel = text_from_exel[1: ]
        text_from_exel = text_from_exel.replace("-", " ")
        return text_from_exel

#print(cut_all_tire("-Саввино, 1 Мая-26-4-1"))

#result = dadata.suggest("address", cut_all_tire("Саввино, 1 Мая-22-22"))
#result = dadata.suggest("address", "Саввино, 1 Мая-22-22")

# for v in result:
#     print(v['unrestricted_value'])

import httpx
import time
try:
    result = dadata.suggest("address", cut_all_tire("Уфа г, Сун-Ят-Сена ул, д.11, кв.138"))
    if result != []:
        for v in result:
            print("Pervoe if " + v['unrestricted_value'])
        time.sleep(1)
    else:
        r = requests.get(f'https://suggest-maps.yandex.ru/v1/suggest?apikey={ya_apikey}&text={"Уфа г, Сун-Ят-Сена ул, д.11, кв.138"}&print_address=1')
        if hasattr(json.loads(r.text), 'results') or 'results' in json.loads(r.text):
            # print(json.loads(r.text)["results"][0]['address']['formatted_address'])   
            result = dadata.suggest("address", json.loads(r.text)["results"][0]['address']['formatted_address'])
            if result != []:
                for v in result:
                    print("Vtoroe if " + v['unrestricted_value'])
                time.sleep(1)
            else:
                print("Netu resultata")
except httpx.ConnectTimeout:
    print("Inet gluk")

#'unrestricted_value'
#г.Уфа Менделеева ул. 128/1, гараж. 25-------------------------------------------------------ne mojet naiti
# СКО, г.Уфа, Черниковская ул., 16-------------------------------------------------------ne mojet naiti
#print(result)
#poisk-----------------Кольцевая д.66, кв. 6
#result------- 443086, Самарская обл, г Самара, Октябрьский р-н, ул Кольцевая, д 66, кв 6
#result------- 450112, Респ Башкортостан, г Уфа, ул Кольцевая, д 66, кв 6
res = []