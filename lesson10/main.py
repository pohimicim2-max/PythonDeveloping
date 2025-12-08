from tkinter import *
from tkinter import messagebox
from funcs import advanced_prison_1488, fake_console_error_trap
import funcs 
import pygame
import os
from funcs import send_warning, send_goodluck
from plyer import notification
import threading
import time
from funcs import Colors
from PIL import Image, ImageTk

os.system("")
pygame.init()

downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
music_file = "RETAILATION.mp3"
music_path = os.path.join(downloads_path, music_file)

TIME_LIMIT = 90
time_left = TIME_LIMIT
timer_running = False
prison_triggered = False

def start_music():
    class Colors:
        RED = '\033[91m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        CYAN = '\033[96m'
        RESET = '\033[0m'

    if os.path.exists(music_path):
        try:
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.play(-1)
            print(f"{Colors.GREEN}МУЗЫКА УСПЕШНО ЗАПУЩЕНА ИЗ:{Colors.RESET} {Colors.YELLOW}{music_path}{Colors.RESET}")
            print(f"{Colors.GREEN}СЕЙЧАС ИГРАЕТ: {music_file}{Colors.RESET}")
            return True
        except Exception as oshibka:
            notification.notify(
                title="ОШИБКА",
                message=f"Не удалось запустить музыку: {oshibka}",
                app_name="Дз Максима (не)",
                timeout=3,
                toast=True,
            )
    else:
        print(f"{Colors.RED}Файл не найден: {music_path}")
        print(f"Пожалуйста, положите музыку в: {downloads_path}{Colors.RESET}")
        notification.notify(
            title="FATAL ERROR MUSIC",
            message=f"МУЗЫКА НЕ НАЙДЕНА, ПОЖАЛУЙСТА, ПОЛОЖИТЕ ЕЕ В: {downloads_path}",
            timeout=3,
            toast=True
        )
        return False

def update_timer():
    global time_left, timer_running
    if time_left > 0 and timer_running:
        time_left -= 1
        timer_label.config(text=f"ОСТАЛОСЬ: {time_left} СЕКУНД")
        
        if time_left == 60:
            try:
                pygame.mixer.music.stop()
                pygame.mixer.music.load(music_path)
                pygame.mixer.music.play(-1, start=89)
                print("Музыка переключена на 1:29 (осталось 60 сек)")
                try:
                    notification.notify(
                        title="СООБЩЕНИЕ МАКСИМА",
                        message=f"ДМИТРИЙ, У МЕНЯ КОД НЕ РАБОТАЕТ, КСТАТИ ОСТАЛОСЬ {time_left} СЕКУНД!",
                        timeout=3
                    )
                except:
                    pass
            except Exception as maksim:
                notification.notify(
                    title="ОШИБКА",
                    message=f"Не удалось переключить музыку: {maksim}",
                    app_name="Дз Максима (не)",
                    timeout=3,
                    toast=True,
                )
        
        if time_left == 30:
            try:
                pygame.mixer.music.stop()
                pygame.mixer.music.load(music_path)
                pygame.mixer.music.play(0, start=235)
            except Exception as Maskim2:
                print(f"ОШИБКА: {Maskim2}")
            try:
                notification.notify(
                    title="СООБЩЕНИЕ МАКСИМА",
                    message=f"ДМИТРИЙ, ОСТАЛОСЬ {time_left} СЕКУНД, А МОЙ КОД ДОСИХПОР НЕ РАБОТАЕТ!",
                    timeout=3,
                    toast=True
                )
            except:
                pass
        
        if time_left <= 30:
            timer_label.config(fg="red")
        elif time_left <= 60:
            timer_label.config(fg="orange")
        
        mainWindow.after(1000, update_timer)
    elif time_left <= 0 and timer_running:
        timer_running = False
        time_up()

def start_timer():
    global timer_running, time_left
    time_left = TIME_LIMIT
    timer_running = True
    timer_label.config(text=f"ОСТАЛОСЬ: {time_left} СЕКУНД", fg="green")
    update_timer()

def stop_timer():
    global timer_running
    timer_running = False

def end_quiz(reason="ВИКТОРИНА ЗАВЕРШЕНА"):
    global prison_triggered
    
    stop_timer()
    
    try:
        pygame.mixer.music.stop()
        pygame.time.delay(100)
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play(0, start=281)
        print(f"Музыка переключена на 4:41 ({reason})")
    except Exception as e:
        print(f"Не удалось переключить музыку: {e}")
    
    for btn in buttons:
        btn.config(state="disabled")
    
    QUEST.config(text=f"{reason}! СЧЁТ: {funcs.get_score()}/{funcs.get_total_questions()}")
    
    if funcs.get_total_questions() > 0 and not prison_triggered:
        percentage = (funcs.get_score() / funcs.get_total_questions()) * 100
        if percentage < 50:
            prison_triggered = True
            mainWindow.after(1000, lambda: funcs.fake_console_error_trap(mainWindow))
    
    try:
        if reason == "ВРЕМЯ ВЫШЛО":
            notification.notify(
                title="ВРЕМЯ ВЫШЛО!",
                message=f"Ваш счёт: {funcs.get_score()} из {funcs.get_total_questions()}",
                timeout=5,
                app_name="Викторина Бобика",
                toast=True,
            )
        else:
            notification.notify(
                title="ВИКТОРИНА ЗАВЕРШЕНА!",
                message=f"Вы ответили на все вопросы! Счёт: {funcs.get_score()}/{funcs.get_total_questions()}",
                timeout=5,
                app_name="Викторина Бобика",
                toast=True
            )
    except Exception as e:
        print(f"Не удалось показать уведомление: {e}")

def time_up():  
    end_quiz("ВРЕМЯ ВЫШЛО")

send_warning()
send_goodluck()

mainWindow = Tk()
width = 700
height = 400

mainWindow.title("ВИКТОРИНА БОБИКА")
mainWindow.resizable(False, False)

screen_width = mainWindow.winfo_screenwidth()
screen_height = mainWindow.winfo_screenheight()

x_offset = (screen_width - width) // 2
y_offset = (screen_height - height) // 2

mainWindow.geometry(f"{width}x{height}+{x_offset}+{y_offset}")

timer_label = Label(text=f"ОСТАЛОСЬ: {TIME_LIMIT} СЕКУНД", font=("Comic Sans MS", 14, "bold"), fg="green")
timer_label.place(anchor="center", relx=0.5, rely=0.05)

QUEST = Label(text="", font=("Comic Sans MS", 16))
QUEST.place(anchor="center", relx=0.5, rely=0.15)

info = Label(text="", font=("Comic Sans MS", 12), fg="red")
info.place(anchor="center", relx=0.5, rely=0.25)

score_label = Label(text="Счёт: 0", font=("Comic Sans MS", 12), fg="blue")
score_label.place(x=10, y=10)

buttons = []

def update_score():
    score_label.config(text=f"Счёт: {funcs.get_score()}")

def on_button_click(idx):
    old_finished = funcs.is_quiz_finished()
    funcs.check_answer(idx, QUEST, buttons, info, score_label)
    update_score()
    if not old_finished and funcs.is_quiz_finished():
        end_quiz("ВИКТОРИНА ЗАВЕРШЕНА")
        stop_timer()
    
    if funcs.is_quiz_finished():
        stop_timer()

for i in range(4):
    btn = Button(width=100, height=1, font=("Comic Sans MS", 14), 
                 command=lambda idx=i: on_button_click(idx))
    btn.place(anchor="center", relx=0.5, rely=0.25 + 0.15 * (i + 1))
    buttons.append(btn)

funcs.init_quiz_by_difficulty("ВСЕ")
funcs.generate_quest(QUEST, buttons, info)
update_score()
start_music()
start_timer()

mainWindow.mainloop()
stop_timer()
