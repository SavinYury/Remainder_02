### ПРОГРАММА НАПОМИНАНИЕ
from tabnanny import check
from tkinter import * # Импортируем из tkinter все функции
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
import time
import datetime
import pygame

t = 0 # Создали (обозначили) переменную t для использования и присвоили нулевое значение
music = False
hour = None
minute = None
text = None
new_window = None

### Создаем функцию установки времени срабатывания
def set():
    global t # Поскольку переменная t используется в двух функциях назначаем ее глобальной
    global hour
    global minute
    global text
    text = sd.askstring(title="Текст напоминания", prompt="Введите текст напоминания.")
    rem = sd.askstring(title="Время напоминания", prompt="Введите время напоминания (чч:мм)") # Создаем переменную куда введут время напоминания
    if rem: # Условие если время введено и переменная не пустая то-
        try: # Используем обработку исключений
            hour = int(rem.split(":")[0]) # Получаем часы из введенной информацией пользователем, делаем целым числом и записываем в список с индексом 0
            minute = int(rem.split(":")[1]) # Получаем минуты из введенной информацией пользователем, делаем целым числом и записываем в список с индексом 1
            now = datetime.datetime.now() # Создаем переменную текущего времени от которого пойдет отсчет
            print(now) # Контрольный вывод информации когда ввели время для напоминания
            dt = now.replace(hour=hour, minute=minute, second=0) # Переменная времени на которое установлено наше напоминание
            print(dt) # Контрольный вывод информации когда сработает напоминание
            t = dt.timestamp() # В переменную положим текущую временную компьютерную метку
            print(t)
            label.config(text=f"Напоминание на {hour:02}:{minute:02} \n{text}")
        except Exception as e:
            mb.showerror(title="Ошибка", message=f"Произошла ошибка {e}") # При вводе значений не в режиме часов минут обрабатываем ошибку


### Создаем функцию проверки совпадения времени (Рекурсия)
def check():
    global t # Поскольку переменная t используется в двух функциях назначаем ее глобальной
    global hour
    global minute
    global text
    global new_window
    if t: # Цикл проверки переменной t что она не пустая
        now = time.time() # Получаем текущее временную компьютерную метку
        print(now)
        if now >= t: # Если текущее время больше установленного времени напоминания то
            new_window = Toplevel()
            new_window.title("Напоминание")
            new_window.geometry("350x250+500+500")
            l = Label(new_window, font=("Arial", 18), text=f"НЕ ЗАБУДЬ {hour:02}:{minute:02} \n{text}")
            l.pack()
            play_snd() # То тогда включаем функцию воспроизведения музыки
            t = 0 # Переменную t обнуляем
    window.after(5000, check) # Рекурсия функция check() вызывает сама себя каждые 10 000 миллисекунд


### Создаем функцию для проигрывания музыки
def play_snd():
    global music  # Назначаем переменную глобальной так как работает в нескольких функциях
    music = True #так как музыка проигрывается то устанавливаем переменной music значение True
    pygame.mixer.init() # Инициализируем миксер в pygame для проигрывания музыки
    pygame.mixer.music.load("reminder.mp3") # Команда на загрузку музыки в миксер
    pygame.mixer.music.play() # Даем команду на проигрывание музыкального файла


### Создаем функцию отключения музыки
def stop_music():
    global music # Назначаем переменную глобальной так как работает в нескольких функциях
    global new_window
    if music: # Если музыка играет и переменная True меняем значение на False
        pygame.mixer.music.stop() # Команда стоп на воспроизведение
        music = False # Присваиваем переменной значение False
        new_window.destroy()
    label.config(text="Установить новое напоминание")


### Создаем графический интерфейс
window = Tk()
window.title("Напоминание") # Меняем название нашего всплывающего окна
width_d = window.winfo_screenwidth() # Создаем переменную запрашивающую ширину подключенного монитора
heidth_d = window.winfo_screenheight() # Создаем переменную запрашивающую высоту подключенного монитора
window.geometry(f"400x200+{(width_d//2+150)}+{(heidth_d//2)}") # Располагаем в центре окна

### Создаем метку
label = Label(text="Установите напоминание", font=("Arial", 14))
label.pack(pady=10)

### Создаем кнопку
set_button = Button(text="Установить напоминание", command=set)
set_button.pack(pady=10)

### Создаем кнопку отключения
stop_button = Button(text="Остановить музыку", command=stop_music)
stop_button.pack(pady=10)

check()

window.mainloop()