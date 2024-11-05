### ПРОГРАММА НАПОМИНАНИЕ
from tkinter import * # Импортируем из tkinter все функции
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
import time
import datetime
import pygame






### Создаем графический интерфейс
window = Tk()
window.title("Напоминание") # Меняем название нашего всплывающего окна
width_d = window.winfo_screenwidth() # Создаем переменную запрашивающую ширину подключенного монитора
heidth_d = window.winfo_screenheight() # Создаем переменную запрашивающую высоту подключенного монитора
window.geometry(f"400x200+{(width_d//2)-200}+{(heidth_d//2)-100}") # Располагаем в центре окна

### Создаем метку
l = Label(text = "Установите напоминание")
l.pack(pady=10)

### Создаем кнопку
set_button = Button(text = "Установить напоминание", command=set)
set_button.pack(pady=10)

window.mainloop()