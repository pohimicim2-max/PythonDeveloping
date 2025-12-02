import tkinter as tk
from tkinter import messagebox

def calculator():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        
        # Выполняем все операции
        results = []
        results.append(f"Сложение: {a} + {b} = {a + b}")
        results.append(f"Вычитание: {a} - {b} = {a - b}")
        results.append(f"Умножение: {a} × {b} = {a * b}")
        
        if b != 0:
            results.append(f"Деление: {a} ÷ {b} = {a / b:.2f}")
        else:
            results.append("Деление: НА 0 ДЕЛИТЬ НЕЛЬЗЯ!")
        
        result_label.config(text="\n".join(results))
        
    except ValueError:
        messagebox.showerror("Ошибка!", "Введите числа!")

# Создаем окно
window = tk.Tk()
window.title("Калькулятор")
window.geometry("300x300")

# Поля ввода
tk.Label(window, text="Первое число:").pack(pady=5)
entry1 = tk.Entry(window, width=30)
entry1.pack(pady=5)

tk.Label(window, text="Второе число:").pack(pady=5)
entry2 = tk.Entry(window, width=30)
entry2.pack(pady=5)

# Кнопка расчета
tk.Button(window, text="Вычислить", command=calculator, bg="lightblue", width=20).pack(pady=10)

# Поле для результата
result_label = tk.Label(window, text="Результат:", justify="left")
result_label.pack(pady=10)

# Запуск приложения
window.mainloop()