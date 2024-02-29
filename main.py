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



s10 = "Балашиха, Пионерская-9-9"#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

d= "Сельская Богородская ул., д. 47, кв. 31"#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
n="Кононенко Виталий"#ETO NUJNO PROVERYAT NA NALICHIE CIFR
n1 = "7 960 391-52-45 - Исходящий звонок" #result['result'] --- None

respond = {'source': 'СКО, г.Уфа, Черниковская ул., 18', 'result': 'г Уфа, ул Черниковская, д 18', 'postal_code': '450038', 'country': 'Россия', 'country_iso_code': 'RU', 'federal_district': 'Приволжский', 'region_fias_id': '6f2cbfd8-692a-4ee4-9b16-067210bde3fc', 'region_kladr_id': '0200000000000', 'region_iso_code': 'RU-BA', 'region_with_type': 'Респ Башкортостан', 'region_type': 'Респ', 'region_type_full': 'республика', 'region': 'Башкортостан', 'area_fias_id': None, 'area_kladr_id': None, 'area_with_type': None, 'area_type': None, 'area_type_full': None, 'area': None, 'city_fias_id': '7339e834-2cb4-4734-a4c7-1fca2c66e562', 'city_kladr_id': '0200000100000', 'city_with_type': 'г Уфа', 'city_type': 'г', 'city_type_full': 'город', 'city': 'Уфа', 'city_area': None, 'city_district_fias_id': None, 'city_district_kladr_id': None, 'city_district_with_type': 'р-н Калининский', 'city_district_type': 'р-н', 'city_district_type_full': 'район', 'city_district': 'Калининский', 'settlement_fias_id': None, 'settlement_kladr_id': None, 'settlement_with_type': None, 'settlement_type': None, 'settlement_type_full': None, 'settlement': None, 'street_fias_id': '0c583cad-0c4b-4c8a-8627-42df03803341', 'street_kladr_id': '02000001000022200', 'street_with_type': 'ул Черниковская', 'street_type': 'ул', 'street_type_full': 'улица', 'street': 'Черниковская', 'stead_fias_id': None, 'stead_kladr_id': None, 'stead_cadnum': None, 'stead_type': None, 'stead_type_full': None, 'stead': None, 'house_fias_id': 'dfd6b708-e674-4c3d-abe9-ff0269437770', 'house_kladr_id': '0200000100002220017', 'house_cadnum': '02:55:000000:41170', 'house_type': 'д', 'house_type_full': 'дом', 'house': '18', 'block_type': None, 'block_type_full': None, 'block': None, 'entrance': None, 'floor': None, 'flat_fias_id': None, 'flat_cadnum': None, 'flat_type': None, 'flat_type_full': None, 'flat': None, 'flat_area': None, 'square_meter_price': '107128', 'flat_price': None, 'postal_box': None, 'fias_id': 'dfd6b708-e674-4c3d-abe9-ff0269437770', 'fias_code': '02000001000000002220017', 'fias_level': '8', 'fias_actuality_state': '0', 'kladr_id': '0200000100002220017', 'capital_marker': '2', 'okato': '80401370000', 'oktmo': '80701000001', 'tax_office': '0273', 'tax_office_legal': '0273', 'timezone': 'UTC+5', 'geo_lat': '54.8111384', 'geo_lon': '56.1057042', 'beltway_hit': None, 'beltway_distance': None, 'qc_geo': 0, 'qc_complete': 9, 'qc_house': 2, 'qc': 1, 'unparsed_parts': 'СКО', 'metro': None}

dadata = Dadata(token, secret)




s9 = "Саввино, 1 Мая-26-4-1"
s12 = "СКО, г.Уфа, Черниковская ул., 18"
#result = dadata.clean("address", s9)
#print(result)
st = "САВВИНО"
st1 = "СКО"
#print(st.lower().capitalize())
#print(select_data("select*from cities where name = ?", (st.lower().capitalize(), )))


# ЕСЛИ ЕСТЬ unparsed_parts ТО МЫ ИСПОЛЬЗУЮЕМ РЕКУЭСТ НА ЯНДЕКС МАПС ...... ЕСЛИ ЕСТЬ ПРЯМОЕ СОВПАДЕНИЕ ГОРОДА ТО ЗАБИРАЕМ FORMATTED_ADDRESS И KIND[HOUSE] ДАЛЕЕ ПОВТОРЯЕМ ОСНОВНОЙ ЗАПРОС .......... НОМЕР КВАРТИРЫ ИЗ ОСНОВНОГО ЗАПРОСА ДОБАВИМ К ФОРМАТТЕД ТАК: ПОЙДЕМ С КОНЦА ОСНОВНОГО ЗАПРОСА И ПРОБЕЖИМСЯ ПО НЕМУ НА СОВПАДЕНИЕ ХАУСА .... ЕСЛИ СОВПАДЕНИЙ НЕСКОЛЬКО ТО ЗАБИРАЕМ ВСЕ ЧТО ЕСТЬ И ВТОРОЕ СОВПАВШЕЕ БУДЕТ КВАРТИРОЙ ЕСЛИ НЕТ ТО ТО ЧТО ПОСЛЕ СОВПАДЕНИЯ (ЧИСЛА) БУДЕТ КВАРТИРОЙ..... ОБНОВЛЕННЫЙ ОСНОВНОЙ ЗАПРПОС БУДЕМ ПОВТОРЯТЬ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


r = requests.get(f'https://suggest-maps.yandex.ru/v1/suggest?apikey={ya_apikey}&text={s9}&print_address=1')

print(json.loads(r.text)["results"][0])
