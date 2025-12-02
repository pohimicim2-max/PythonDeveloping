import tkinter as tk
import random
import time
from tkinter import messagebox

# Основное окно
window = tk.Tk()
window.title("Домашние задания")
window.geometry("400x500")

# ===================== ДЗ 1: ШАРМАНКА =====================
def dz1_sharmanka():
    dz1_window = tk.Toplevel(window)
    dz1_window.title("ДЗ 1 - ШАРМАНКА")
    dz1_window.geometry("300x200")
    
    result_label = tk.Label(dz1_window, text="", font=("Arial", 24))
    result_label.pack(pady=20)
    
    def generate_number():
        number = random.randint(1, 1000)
        result_label.config(text=str(number), fg="green")
    
    tk.Button(dz1_window, text="ЗАПУСТИТЬ ШАРМАНКУ", 
             command=generate_number, bg="green", fg="white").pack(pady=10)

# ===================== ДЗ 2: РАДУЖНАЯ ШАРМАНКА =====================
def dz2_rainbow_sharmanka():
    dz2_window = tk.Toplevel(window)
    dz2_window.title("ДЗ 2 - РАДУЖНАЯ ШАРМАНКА")
    dz2_window.geometry("600x200")
    
    frame = tk.Frame(dz2_window)
    frame.pack(pady=20)
    
    number_labels = []
    for i in range(11):
        label = tk.Label(frame, text="", font=("Arial", 20), width=3)
        label.pack(side=tk.LEFT, padx=5)
        number_labels.append(label)
    
    def generate_rainbow():
        colors = ["red", "orange", "yellow", "green", "blue", 
                 "dark blue", "purple", "pink", "brown", "gray", "cyan"]
        
        for i in range(11):
            number = random.randint(0, 9)
            number_labels[i].config(text=str(number), fg=colors[i])
    
    tk.Button(dz2_window, text="ЗАПУСТИТЬ РАДУЖНУЮ ШАРМАНКУ", 
             command=generate_rainbow, bg="purple", fg="white").pack(pady=10)

# ===================== ДЗ 3: ГЕНЕРАТОР НОМЕРОВ =====================
def dz3_phone_generator():
    dz3_window = tk.Toplevel(window)
    dz3_window.title("ДЗ 3 - ГЕНЕРАТОР НОМЕРОВ")
    dz3_window.geometry("500x250")
    
    phone_label = tk.Label(dz3_window, text="", font=("Arial", 24, "bold"))
    phone_label.pack(pady=30)
    
    def generate_phone():
        region = ''.join([str(random.randint(0, 9)) for _ in range(3)])
        first_part = ''.join([str(random.randint(0, 9)) for _ in range(3)])
        second_part = ''.join([str(random.randint(0, 9)) for _ in range(2)])
        third_part = ''.join([str(random.randint(0, 9)) for _ in range(2)])
        
        phone_number = f"+7 ({region}) {first_part}-{second_part}-{third_part}"
        phone_label.config(text=phone_number, fg="blue")
    
    def copy_phone():
        phone = phone_label.cget("text")
        if phone:
            dz3_window.clipboard_clear()
            dz3_window.clipboard_append(phone)
            messagebox.showinfo("СКОПИРОВАНО", f"Номер {phone} скопирован!")
    
    tk.Button(dz3_window, text="СГЕНЕРИРОВАТЬ НОМЕР", 
             command=generate_phone, bg="blue", fg="white", font=("Arial", 14)).pack(pady=10)
    
    tk.Button(dz3_window, text="КОПИРОВАТЬ НОМЕР", 
             command=copy_phone, bg="green", fg="white").pack(pady=5)

# ===================== ОСНОВНОЕ МЕНЮ =====================
tk.Label(window, text="ДОМАШНИЕ ЗАДАНИЯ", 
        font=("Arial", 20, "bold"), fg="darkblue").pack(pady=20)

tk.Label(window, text="Выберите задание:", 
        font=("Arial", 12)).pack(pady=10)

# Кнопки для ДЗ
tk.Button(window, text="ДЗ 1: ШАРМАНКА", 
         command=dz1_sharmanka, bg="green", fg="white", 
         width=20, height=2, font=("Arial", 12)).pack(pady=10)

tk.Button(window, text="ДЗ 2: РАДУЖНАЯ ШАРМАНКА", 
         command=dz2_rainbow_sharmanka, bg="purple", fg="white", 
         width=20, height=2, font=("Arial", 12)).pack(pady=10)

tk.Button(window, text="ДЗ 3: ГЕНЕРАТОР НОМЕРОВ", 
         command=dz3_phone_generator, bg="blue", fg="white", 
         width=20, height=2, font=("Arial", 12)).pack(pady=10)

# Информация
tk.Label(window, text="\nПростой и понятный интерфейс\nдля выполнения домашних заданий", 
        font=("Arial", 10), fg="gray").pack(pady=20)

# Запуск приложения
window.mainloop()