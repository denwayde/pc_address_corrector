from tkinter import *
from tkinter import ttk, filedialog
from datetime import datetime as dt 


root = Tk()
root.title("Нормализатор адресов в Excel таблице")
# Функция для обработки нажатия кнопки "Browse"



def display():
    label['text'] = entry.get()

def browse_file():
    filename = filedialog.askopenfilename()
    entry.configure(state="normal")
    #entry.configure(text = filename)
    entry.insert(0, filename)
    entry.configure(state="disabled")

label = ttk.Label(text="Выберите excel - файл для нормализации адресов")
label.grid(column=0, row=0, sticky="w", pady=(10, 0))

entry = ttk.Entry(state="disabled")
entry.grid(column=0, row=1, padx=4, pady=4, sticky="ew")

btn = ttk.Button(text="Выбрать файл", width=20, command=browse_file)
btn.grid(column=1, row=1, padx=4, pady=4, sticky="w")

label = ttk.Label()
label.grid(column=0, row=2, sticky="w")

editor = Text(width=55, height=15, state="normal", background="#002451", foreground="#CCCCB4")
editor.grid(column=0, row=3, padx=(4,0), pady=(4,20), sticky="w")
editor.insert(END, "New string")
editor.configure(state="disabled")

ys = ttk.Scrollbar(orient = "vertical", command = editor.yview)
ys.grid(column = 1, row = 3, pady=(4,20), sticky = "wsn")
editor["yscrollcommand"] = ys.set

btn = ttk.Button(text="Отмена", width=20, command=display)
btn.grid(column=1, row=4, padx=4, pady=(0, 4), sticky="w")


label = ttk.Label(text=f"Copyright {dt.now().year}. G.D.R.")
label.grid(column=0, row=4, sticky="ew", pady=(10, 0), padx=4)

root.geometry("600x400")
root.mainloop()