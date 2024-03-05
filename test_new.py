import requests
import json
from dadata import Dadata
from dotenv import load_dotenv
import os
import string
import re
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Border, Side
import httpx
import time
# Загружаем переменные из файла .env
load_dotenv()
# Пример использования переменных
token = os.getenv("TOKEN")
secret = os.getenv("SECRET")
ya_apikey = os.getenv("YA_APIKEY")

border_style = Border(right=Side(style='thin'), top=Side(style='thin'), bottom=Side(style='thin'))
font_style = Font(bold=False, size=10)
fill = PatternFill(start_color="FFFF00", end_color="FFFF00", fill_type="solid")

def is_punctuation(char):
    return char in string.punctuation

def cut_all_tire(text_from_exel):
    if is_punctuation(text_from_exel[0]):
        text_from_exel = text_from_exel[1: ]
        text_from_exel = text_from_exel.replace("-", " ")
    return text_from_exel


def dadata_proccess(req): 
    print("ETO REQ "+ str(req))
    try:#"Уфа г, Сун-Ят-Сена ул, д.11, кв.138"
        dadata = Dadata(token, secret)
        final_result = ''
        result = dadata.suggest("address", req)
        print(result)
        if result != []:
            print(result[0]['unrestricted_value'])
            final_result = result[0]['unrestricted_value']
        #dadata.close()
        print("IZ DATA PROCCESS"+final_result)
        time.sleep(1)
        return final_result   
    except httpx.ConnectTimeout:
        print('Прерыв соединения с удаленным сервером')
        #return "Ошибка при обработке запроса" 
        
            

def ya_maps_proccess(req):
    r = requests.get(f'https://suggest-maps.yandex.ru/v1/suggest?apikey={ya_apikey}&text={req}&print_address=1')
    final_result = ''
    if hasattr(json.loads(r.text), 'results') or 'results' in json.loads(r.text):
        final_result = json.loads(r.text)["results"][0]['address']['formatted_address']
    return final_result 

def result_from_apis(req):###-----------------------chto to ne to imenno zdes
    print("IZ RESULT FROM API "+req)
    res = dadata_proccess(cut_all_tire(req))
    if res == []:
        res1 = dadata_proccess(req)
        if res1 == []:
            res3 = ya_maps_proccess(req)
            if res3 == []:
                print("res from ya api" + dadata_proccess(ya_maps_proccess(cut_all_tire(req))))
                return dadata_proccess(ya_maps_proccess(cut_all_tire(req)))
            else:
                print("samii finalnii res"+ dadata_proccess(res3))
                return dadata_proccess(res3)
        else:
            print("eto vtoroi res"+ dadata_proccess(req))
            return res1
    else:
        print("eto pervii result"+ dadata_proccess(cut_all_tire(req)))
        return res

def this_phone_num(text_from_exel):
    final_result = True
    digit = 0
    for v in text_from_exel:
        if v.isdigit():
            digit = digit + 1
    if digit == 0 or digit >= 11:
        final_result = False
    return final_result

from openpyxl.utils.exceptions import InvalidFileException


def excel_procces(file_name):#VASHE NE POIMU CHTO NE TAK
    wb = load_workbook(file_name)#'Arc.xlsx'
    # Выбираем активный лист
    sheet = wb.active
    sheet.column_dimensions['H'].width = 60
    for idx, row in enumerate(sheet.iter_rows(min_row=2, min_col=1, max_col=1, values_only=True), start=2): 
        try:
            value_a = row[0]
            if this_phone_num(value_a):
                # print("11111 "+value_a)
                sheet.cell(row = idx, column=8, value = result_from_apis(value_a))     
            else:
                sheet.cell(row = idx, column=8, value = f"В ячейке A[{idx}] не адрес")
            cell = sheet.cell(row=idx, column=8)
            cell.border = border_style
            cell.font = font_style
            sheet.cell(row=1, column=8, value='Адреса').font = Font(bold=True)
            sheet.cell(row=1, column=8, value='Адреса').border = border_style
        except InvalidFileException as e:
            print(f'Ошибка при обращении к файлу: {e}')
        except IndexError:
            print("Vishli za predeli")
        except Exception as e:
            print(f'Произошла непредвиденная ошибка: {e}')
    wb.save(file_name)       
    print("Vse zapisano")


excel_procces('Arc.xlsx')
        
            


#'unrestricted_value'
#г.Уфа Менделеева ул. 128/1, гараж. 25-------------------------------------------------------ne mojet naiti
# СКО, г.Уфа, Черниковская ул., 16-------------------------------------------------------ne mojet naiti
#print(result)
#poisk-----------------Кольцевая д.66, кв. 6
#result------- 443086, Самарская обл, г Самара, Октябрьский р-н, ул Кольцевая, д 66, кв 6
#result------- 450112, Респ Башкортостан, г Уфа, ул Кольцевая, д 66, кв 6
res = []