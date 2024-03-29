from tkinter import *
from tkinter import ttk, filedialog
from datetime import datetime as dt 
from test_new import excel_procces
import asyncio


root = Tk()
root.title("Нормализатор адресов в Excel таблице")
# Функция для обработки нажатия кнопки "Browse"



def display():
    label['text'] = entry.get()

#filename_global = StringVar()

def browse_file():
    filename = filedialog.askopenfilename(filetypes=[('Excel files', '*.xlsx')])
    entry.configure(state="normal")
    # filename_global = filename
    entry.insert(0, filename)
    entry.configure(state="disabled")


def click():
    window = Tk()
    window.title("Внимание")
    window.geometry("250x200")
    label = ttk.Label(window, text=" Файл который Вы\nсобераетесь редактировать,\nдолжен быть закрыт", justify="center")
    label.pack(expand=1)
    close_button = ttk.Button(window, text="Начинаем", command=lambda: start(window))
    close_button.pack(anchor="center", expand=1)


def start(window):
    window.destroy()  # закрываем окно "Внимание"
    #asyncio.create_task(excel_procces(entry.get(), dispaly_text))
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(excel_procces(entry.get(), dispaly_text))


# def start(window):
#     asyncio.run(excel_procces(entry.get(), dispaly_text))
#     asyncio.run(close(window))
    

async def close(window):
    await window.destroy()    

async def dispaly_text(new_string):
    editor.configure(state="normal")
    editor.insert(END, new_string+"\n")
    editor.configure(state="disabled")
    editor.update_idletasks()
    await asyncio.sleep(0.1)

label = ttk.Label(text="Выберите excel - файл для нормализации адресов")
label.grid(column=0, row=0, sticky="w", pady=(10, 0))

entry = ttk.Entry(state="disabled")
entry.grid(column=0, row=1, padx=4, pady=4, sticky="ew")

btn = ttk.Button(text="Выбрать файл", width=20, command=browse_file)
btn.grid(column=1, row=1, padx=4, pady=4, sticky="w")

btn1 = ttk.Button(text="Пуск", width=20, command=click)
btn1.grid(column=2, row=1, padx=4, pady=4, sticky="w")

label = ttk.Label()
label.grid(column=0, row=2, sticky="w")

editor = Text(width=55, height=15, state="disabled", background="#002451", foreground="#CCCCB4")
editor.grid(column=0, row=3, padx=(4,0), pady=(4,20), sticky="ew")


ys = ttk.Scrollbar(orient = "vertical", command = editor.yview)
ys.grid(column = 1, row = 3, pady=(4,20), sticky = "wsn")
editor["yscrollcommand"] = ys.set

btn = ttk.Button(text="Отмена", width=20, command=lambda: root.destroy())
btn.grid(column=2, row=4, padx=4, pady=(0, 4), sticky="w")


label = ttk.Label(text=f"Copyright {dt.now().year}. G.D.R.")
label.grid(column=0, row=4, sticky="ew", pady=(10, 0), padx=4)

root.geometry("725x400")
root.mainloop()
