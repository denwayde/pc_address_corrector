import sqlite3

with open("cities.txt", "r", encoding="UTF-8") as file:
    content = file.read()

countries_arr = content.split("\n")

my_countries_arr = []
for z in countries_arr:
    arr = z.split("\t")
    if arr[0].isnumeric() and  "(" not in arr[2] and "`" not in arr[2]: #---------если есть () удаляй или не вставляй или точка
        my_countries_arr.append((int(arr[0]), int(arr[1]), arr[2]))

#print(my_countries_arr)

con = sqlite3.connect("data.db")
cursor = con.cursor()
cursor.executemany("INSERT INTO cities (city_id, country_id, name) VALUES (?, ?, ?)", my_countries_arr)
con.commit()
# данные для добавления
# people = [("Sam", 28), ("Alice", 33), ("Kate", 25)]
# cursor.executemany("INSERT INTO people (name, age) VALUES (?, ?)", people)
 
