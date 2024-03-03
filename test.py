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




import string

def is_punctuation(char):
    return char in string.punctuation

def check_none(text_from_respond):
    if text_from_respond == None or len(text_from_respond)==0:
        text_from_respond = ''
    return text_from_respond

def is_none(text_from_respond):
    if text_from_respond == None:
        return False
    return True

import re 
#<re.Match object; span=(25, 27), match='1,'>
def addr_right_proccess(addrr):
    procceed=''
    mtc = re.search(r'\d+[a-zA-Zа-яА-Я]?[\,\s\-\.\b]?', addrr)
    #print("mtc---------------" + str(mtc))
    if mtc != None:
        #print("mtc.group()---------------" + str(mtc.group()))
        addr_right = addrr[addrr.find(mtc.group())+len(mtc.group()) : ]#poluchili to chto sprava ot naidennogo chisla
        #print("addr_right---------------"+str(addr_right))
        return addr_right_proccess(addr_right)
    else:
        if addrr != '':
            procceed = ', ' + addrr
            procceed = procceed.replace("  ", " ")
        else:
            procceed = addrr
        return procceed
    
n="Кононенко Виталий"#ETO NUJNO PROVERYAT NA NALICHIE CIFR
n1 = "7 960 391-52-45 - Исходящий звонок" #result['result'] --- None
s13 = "г.Уфа Менделеева ул. 128/1, гараж. Бокс 26"
sss = "Белорецк г, Ленина , 71, ооол"
s14 = "Межгорье г, Олимпийская ул, 3, кв.42" 
s15 = "Белорецк г, Точисского , 15а, 44988"

#print("VIVOD------------------"+ addr_right_proccess(s15))

text_from_exel = ''
right_end = addr_right_proccess(s15)
if right_end != '':
    text_from_exel = s15[ :s15.find(right_end)]
    print("right_end------------------- NE pustoi " + s15[ :s15.find(right_end)])
else:
    print("right_end-------------------pustoi")

# print(s13[s13.find(mtc)+len(mtc) : ])

# result = dadata.suggest('address', sss)
# print(result)

# r = requests.get(f'https://suggest-maps.yandex.ru/v1/suggest?apikey={ya_apikey}&text={sss}&print_address=1')
# print(json.loads(r.text)["results"][0]['address'])

# check_location_arr = {}
# house = ''
# for x in json.loads(r.text)["results"][0]['address']['component']:
#     if x['kind'] == ['LOCALITY']:
#         check_location_arr['local'] = x['name']
#     if x['kind'] == ['STREET']:
#         st = ''
#         for z in x['name'].split(' '):
#             if z.istitle():
#                st = st+" "+z 
#         st = st.lstrip()
#         check_location_arr['street'] = st
#     if x['kind'] == ['HOUSE']:
#         house = x['name']


# house_count = text_from_exel.count(house)
# if house_count == 0:
#     street_index = text_from_exel.find(check_location_arr['street'])
#     substr_right = text_from_exel[street_index+len(check_location_arr['street']) : ] 
#     #print(s13[street_index+len(check_location_arr['street']) : ])

#     substr_right_right = ''
#     for c in substr_right:
#         if is_punctuation(c):
#             punct_index = substr_right.find(c)
#             substr_right_right = substr_right[punct_index + len(c) : ]
#             substr_right_right = ", " + substr_right_right
#             substr_right_right = substr_right_right.replace("  ", " ")
#             break

# result1 = dadata.suggest("address", check_location_arr['local']+" "+check_location_arr['street']+ " " + house)
# if result1 != []:
#     final_result = result1[0]['data']['postal_code']+", "+result1[0]['data']['region']+", "+result1[0]['data']['city_with_type']+", "+result1[0]['data']['street_with_type']+", "+substr_right_right
# else:
#     final_result = "Невозможно преобразовать адрес. Error: in home length = 0"


# print(final_result)