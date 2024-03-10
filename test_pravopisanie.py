import requests
import json
from dadata import Dadata
from dotenv import load_dotenv
import os
import string
import re
from openpyxl import load_workbook
import httpx
from openpyxl.styles import Font, PatternFill, Border, Side
# Загружаем переменные из файла .env
load_dotenv()
# Пример использования переменных
token = os.getenv("TOKEN")
secret = os.getenv("SECRET")
ya_apikey = os.getenv("YA_APIKEY")



s = "сКомсомольск, Горная, 1, 6"
s1 ="гУчалы, сКирова , 8, 17"
s2 = "сАскарово, Учалинская ул, 18/а, 17"


def correct_location(s1):
    m = re.findall(r'[а-яa-z][А-Я]', s1)
    if m != []:
        for x in m:
            r = x[0]+". "+x[1]
            #print(r)
            s1 = s1.replace(x, r)
    return s1

print(correct_location(s2))

def correct_street(s1):
    m = re.findall(r'\d\/[а-яА-Яa-zA-Z]', s1)
    if m != []:
        for x in m:
            r = x.replace("/", "")
            s1 = s1.replace(x, r)
    return s1

print(correct_street(correct_location(s2)))


dadata = Dadata(token, secret)
    
result = dadata.suggest("address", correct_street(correct_location(s2)))

print(result[0]['unrestricted_value'])