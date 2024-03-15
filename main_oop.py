from tkinter import *
from tkinter import ttk, filedialog
from datetime import datetime as dt 
from test_new import excel_procces
import asyncio


class Gui(Tk):
    def __init__(self, loop) -> None:
        self.loop = loop
        self.root = Tk()
        self.root.title("Нормализатор адресов в Excel таблице")
        label = ttk.Label(text="Выберите excel - файл для нормализации адресов")
        label.grid(column=0, row=0, sticky="w", pady=(10, 0))

        self.entry = ttk.Entry(state="disabled")
        self.entry.grid(column=0, row=1, padx=4, pady=4, sticky="ew")

        btn = ttk.Button(text="Выбрать файл", width=20, command= self.browse_file)
        btn.grid(column=1, row=1, padx=4, pady=4, sticky="w")

        btn1 = ttk.Button(text="Пуск", width=20, command= self.click)
        btn1.grid(column=2, row=1, padx=4, pady=4, sticky="w")

        label = ttk.Label()
        label.grid(column=0, row=2, sticky="w")

        self.editor = Text(width=55, height=15, state="disabled", background="#002451", foreground="#CCCCB4")
        self.editor.grid(column=0, row=3, padx=(4,0), pady=(4,20), sticky="ew")


        ys = ttk.Scrollbar(orient = "vertical", command = self.editor.yview)
        ys.grid(column = 1, row = 3, pady=(4,20), sticky = "wsn")
        self.editor["yscrollcommand"] = ys.set

        btn = ttk.Button(text="Отмена", width=20, command=lambda: self.root.destroy())
        btn.grid(column=2, row=4, padx=4, pady=(0, 4), sticky="w")


        label = ttk.Label(text=f"Copyright {dt.now().year}. G.D.R.")
        label.grid(column=0, row=4, sticky="ew", pady=(10, 0), padx=4)
    
    async def show(self):
        while True:
            self.root.update()
            await asyncio.sleep(.1)
    
    async def dispaly_text(self, new_string):
        self.editor.configure(state="normal")
        self.editor.insert(END, new_string+"\n")
        self.editor.configure(state="disabled")
        self.editor.update_idletasks()
        await asyncio.sleep(0)

    def browse_file(self):
        filename = filedialog.askopenfilename(filetypes=[('Excel files', '*.xlsx')])
        self.entry.configure(state="normal")
        # filename_global = filename
        self.entry.insert(0, filename)
        self.entry.configure(state="disabled")
    
    def click(self):
        self.window = Tk()
        self.window.title("Внимание")
        self.window.geometry("250x200")
        label = ttk.Label(self.window, text=" Файл который Вы\nсобераетесь редактировать,\nдолжен быть закрыт", justify="center")
        label.pack(expand=1)
        close_button = ttk.Button(self.window, text="Начинаем", command=lambda: self.loop.create_task(self.start(self.window)))
        close_button.pack(anchor="center", expand=1)

    async def start(self, window):
        window.destroy()  # закрываем окно "Внимание"
        await asyncio.sleep(.1)
        await excel_procces(self.entry.get(), self.dispaly_text)
        # loop = asyncio.new_event_loop()
        # asyncio.set_event_loop(loop)
        # loop.run_until_complete(excel_procces(self.entry.get(), self.dispaly_text))


class App:
    async def exec(self):
        self.window = Gui(asyncio.get_event_loop())
        await self.window.show()

asyncio.run(App().exec())