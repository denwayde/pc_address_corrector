# -*- coding: utf-8 -*-
import requests
import json
from dadata import Dadata
from dotenv import load_dotenv
import os
from db_func import delete_or_insert_data, select_data

# Загружаем переменные из файла .env
load_dotenv()
# Пример использования переменных
token = os.getenv("TOKEN")
secret = os.getenv("SECRET")
ya_apikey = os.getenv("YA_APIKEY")
dadata = Dadata(token, secret)

def substr_right_proccess(substr_right):
    if substr_right != '':
        if not substr_right[0].isalpha():
            substr_right = substr_right[1: ]
            if "кв" in substr_right.lower():
                substr_right = ", "+ substr_right
            else:
                substr_right = ", кв "+ substr_right
        else:
            substr_right = ", "+ substr_right
        substr_right = substr_right.replace("  ", " ")
    else:
        substr_right = ''
    return substr_right 

s10 = "Балашиха, Пионерская-9-9"#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
d= "Сельская Богородская ул., д. 47, кв. 31"#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
n="Кононенко Виталий"#ETO NUJNO PROVERYAT NA NALICHIE CIFR
n1 = "7 960 391-52-45 - Исходящий звонок" #result['result'] --- None
s9 = "Никольско-Архангельский, Болотная-1А-18"
s12 = "СКО, г.Уфа, Черниковская ул., 18"
s13 = "г.Уфа Менделеева ул. 128/1, гараж. Бокс 26"
sn = "7 960 391-52-45 - Исходящий звонок"
sn1 = "Хасанов Фаниль Раильевич"
s14 = "г. Уфа , Борисоглебская, 30/1, 21"


def address_proccess(text_from_exel):
    result = dadata.suggest("address", text_from_exel)
    if result != []:
        final_result = ''
        #print(result[0])
        #print(result[0]['data']['house'])
        value = result[0]['value']
        house = result[0]['data']['house']
        unrestricted_result = result[0]['unrestricted_value']
        # print(unrestricted_result)
        postal_code = result[0]['data']['postal_code']
        index = text_from_exel.find(house)
        substr_right = text_from_exel[index+len(house): ]
        house_result_index = value.find(house)
        substr_result_left = value[ :house_result_index+len(house)]
        flat = substr_right_proccess(substr_right)
        final_result = postal_code + ", " + substr_result_left + flat
        return final_result
    else:
        #print("Netu rezultata poiska v dadata")
        r = requests.get(f'https://suggest-maps.yandex.ru/v1/suggest?apikey={ya_apikey}&text={text_from_exel}&print_address=1')
        if hasattr(json.loads(r.text), 'results') or 'results' in json.loads(r.text):
            city = json.loads(r.text)["results"][0]['address']['component'][1]['name']
            district = json.loads(r.text)["results"][0]['address']['component'][2]['name'].split(' ')
            check_location_arr = [city, *district]
            print(check_location_arr)
            is_valid_location = False
            for x in check_location_arr:
                if x.lower() in text_from_exel.lower():
                    #print("location est")
                    is_valid_location = True 
                    break
            if is_valid_location==True:
                house = ''
                for z in json.loads(r.text)["results"][0]['address']['component']:
                    if z['kind'] == ['HOUSE']:
                        house = z['name']
                #house = json.loads(r.text)["results"][0]['address']['component'][-2]['name']
                index = text_from_exel.find(house)
                substr_right = text_from_exel[index + len(house): ]
                flat = substr_right_proccess(substr_right)
                formatted_address = json.loads(r.text)["results"][0]['address']['formatted_address'] + flat
                address_proccess(formatted_address)
        else:
            final_result = "Невозможно преобразовать адрес"
            return final_result

print(address_proccess(s13))

