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


s10 = "Балашиха, Пионерская-9-9"#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
d= "Сельская Богородская ул., д. 47, кв. 31"#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
n="Кононенко Виталий"#ETO NUJNO PROVERYAT NA NALICHIE CIFR
n1 = "7 960 391-52-45 - Исходящий звонок" #result['result'] --- None
s9 = "Никольско-Архангельский, Болотная-1А-18"
s12 = "СКО, г.Уфа, Черниковская ул., 18"
s13 = "Реутов, Молодежная-4-194"
#print(st.lower().capitalize())
#print(select_data("select*from cities where name = ?", (st.lower().capitalize(), )))

result = dadata.suggest("address", s9)
print(result[0])

# if str(result[0]['area']) in s9 or str(result[0]['city']) in s9:
#     print('lOKATION EST')
#     print(result['postal_code']+", "+result['result'])    
# else:
#     print("NETU LOCATION")
#     #'address': {'formatted_address': 'Московская область, Балашиха, микрорайон Саввино, улица 1 Мая, 26, подъезд 1',}
#     r = requests.get(f'https://suggest-maps.yandex.ru/v1/suggest?apikey={ya_apikey}&text={s9}&print_address=1')
#     #print(json.loads(r.text)["results"][0])
#     city = json.loads(r.text)["results"][0]['address']['formatted_address'].split(',')[1].strip()
#     district = json.loads(r.text)["results"][0]['address']['formatted_address'].split(',')[2].strip()
#     check_location_arr = [city, *district.split(' ')]
#     #print(check_location_arr)
#     is_valid_location = False
#     for x in check_location_arr:
#         if x.lower() in s9.lower():
#             #print("location est")
#             is_valid_location = True
#     if is_valid_location==True:
#         print("location est v yandex")####TUT NADO ZABIRAT IZ YA_REQUEST NOMER DOMA OTREZAT IZ S9 VSE CHTO SPRAVA ZANOSIT V NOVUU STROKU DELAT NOVII ZAPROS K DADATA I ZANOSIT V YACHEIKU
#         #print(json.loads(r.text)["results"][0]['address']['component'][-2]['name'])
#         house = json.loads(r.text)["results"][0]['address']['component'][-2]['name']
#         index = s9.find(house)
#         if index != -1:
#             subst_part = s9[index + len(house): ]
#             flat = ''
#             if subst_part[0].isdigit():
#                 flat = ", кв " + subst_part
#                 #print(flat)
#             else:
#                 flat = ", кв " + subst_part[1:]
#                 #print("substr_flat "+flat)
#             formatted_address = json.loads(r.text)["results"][0]['address']['formatted_address'] + flat
#             corrected_result = dadata.clean("address", formatted_address)
#             # print(formatted_address)
#             #corrected_result['result'] --- Московская обл, г Балашиха, мкр Саввино, ул 1 Мая, д 26, кв 4
#             #corrected_result['postal_code'] ---- '143985'
#             flat_index = corrected_result['result'].find("кв ")
#             #corrected_result['postal_code'] + ", " +corrected_result['result'][:flat_index-2]+flat -----тут как надо!!!!!!!!!!!!!!!!!!!!!!!!!!
#             print(corrected_result['postal_code'] + ", " +corrected_result['result'][:flat_index-2]+flat)

#     else:
#         print("lok_fucked")#TUT MI OSTAVLYAEM YACHEIKU V EXCEL PUSTOI

    


# r = requests.get(f'https://suggest-maps.yandex.ru/v1/suggest?apikey={ya_apikey}&text={s9}&print_address=1')

# print(json.loads(r.text)["results"][0])
