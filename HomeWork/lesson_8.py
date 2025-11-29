import random
import tkinter as tk
from tkinter import messagebox
import time
import os
import webbrowser
messagebox.showinfo("ВНИМАНИЕ", "СОВЕТУЮ ТЕСТИРОВАТЬ КОД С ОТКРЫТЫМ ТЕРМИНАЛОМ")
messagebox.showerror("ВНИМАНИЕ!", "НЕ ДЕЛИТЕ НА 0. Я ВАС ПРЕДУПРЕЖДАЛ.")
print("ПОЛЬЗОВАТЕЛЬ ЗАКРЫЛ ИНФОРМАЦИЮ С ТЕРМИНАЛОМ!!!")
print("ЕСЛИ ВЫ ВИДИТЕ ЭТО СООБЩЕНИЕ, ЗНАЧИТ ВЫ НЕ МАКАН!")


def max_interrogation():

    
    interrogation = tk.Toplevel()
    interrogation.title(" ДОПРОС ПО ДЕЛУ MAX ")
    interrogation.attributes('-fullscreen', True)
    interrogation.configure(bg='#2c3e50')
    interrogation.attributes('-topmost', True)
    
    
    interrogation.protocol("WM_DELETE_WINDOW", lambda: None)
    interrogation.resizable(False, False)
    interrogation.bind('<F11>', lambda e: "break")
    interrogation.bind('<Escape>', lambda e: "break")
    interrogation.bind('<Alt-F4>', lambda e: "break")
    interrogation.bind('<Control-w>', lambda e: "break")
    interrogation.bind('<Control-q>', lambda e: "break")
    
    main_frame = tk.Frame(interrogation, bg='#2c3e50')
    main_frame.place(relx=0.5, rely=0.4, anchor='center')
    
   
    title_label = tk.Label(
        main_frame,
        text=" ДОПРОС ПО ДЕЛУ MAX ", 
        font=("Arial", 36, "bold"), 
        fg="#e74c3c",  
        bg='#2c3e50'
    )
    title_label.pack(pady=30)
    
    question_label = tk.Label(
        main_frame,
        text="ПОЧЕМУ ВЫ ДО СИХ ПОР НЕ СКАЧАЛИ МЕССЕНДЖЕР MAX?", 
        font=("Arial", 20, "bold"), 
        fg="#ecf0f1", 
        bg='#2c3e50',
        wraplength=1000,
        justify="center"
    )
    question_label.pack(pady=20)
    
    
    reasons_frame = tk.Frame(main_frame, bg='#2c3e50')
    reasons_frame.pack(pady=30)
    
    selected_reason = tk.StringVar(value="")
    
    reasons = [
        ("Я ИСПОЛЬЗУЮ ДРУГОЙ МЕССЕНДЖЕР", "other_app"),
        ("НЕ ХВАТАЕТ МЕСТА НА ТЕЛЕФОНЕ", "no_space"),
        ("НЕ ЗНАЛ ПРО МАКС", "dont_know"),
        ("СЛИШКОМ СЛОЖНО УСТАНАВЛИВАТЬ", "too_hard"),
        ("МНЕ ПРОСТО ЛЕНЬ", "lazy"),
        ("Я ПРОТИВ ПРОГРЕССА", "against_progress"),
        ("МОИ ДРУЗЬЯ НЕ ИСПОЛЬЗУЮТ МАКС", "friends_dont_use"),
        ("Я НЕНАВИЖУ МАКС", "bot")
    ]
    
    for i, (reason_text, reason_value) in enumerate(reasons):
        rb = tk.Radiobutton(
            reasons_frame,
            text=reason_text,
            variable=selected_reason,
            value=reason_value,
            font=("Arial", 14),
            fg="#bdc3c7",
            bg='#2c3e50',
            selectcolor='#34495e',
            activebackground='#2c3e50',
            activeforeground='#3498db'
        )
        rb.pack(anchor='w', pady=8)
    
    
    custom_reason_frame = tk.Frame(main_frame, bg='#2c3e50')
    custom_reason_frame.pack(pady=20)
    
    tk.Label(
        custom_reason_frame,
        text="ИЛИ НАПИШИТЕ СВОЮ ПРИЧИНУ:", 
        font=("Arial", 12), 
        fg="#95a5a6", 
        bg='#2c3e50'
    ).pack(anchor='w')
    
    custom_reason_entry = tk.Entry(
        custom_reason_frame,
        font=("Arial", 14),
        width=50,
        bg='#34495e',
        fg='#ecf0f1',
        insertbackground='white'
    )
    custom_reason_entry.pack(pady=10, fill='x')
    
    # КНОПКА ОТПРАВКИ
    def submit_interrogation():
        if not selected_reason.get() and not custom_reason_entry.get().strip():
            messagebox.showwarning("ОШИБКА", "ВЫБЕРИТЕ ПРИЧИНУ ИЛИ НАПИШИТЕ СВОЮ!")
            return
        
        reason = selected_reason.get() if selected_reason.get() else f"custom: {custom_reason_entry.get()}"
        
        
        try:
            with open("max_interrogation_log.txt", "a", encoding="utf-8") as f:
                f.write(f"{time.ctime()}: {reason}\n")
        except:
            pass
        
        interrogation.destroy()
        messagebox.showinfo("ПРОТОКОЛ ЗАВЕРШЕН", "ВАШ ОТВЕТ ЗАПИСАН. НАДЕЕМСЯ, ВЫ ПЕРЕСМОТРИТЕ СВОЕ РЕШЕНИЕ!")
    
    submit_button = tk.Button(
        main_frame,
        text=" ПОДПИСАТЬ ПРОТОКОЛ ДОПРОСА", 
        font=("Arial", 16, "bold"),
        bg="#dfe622", 
        fg="white",
        width=30,
        height=2,
        command=submit_interrogation
    )
    submit_button.pack(pady=30)
    
    
    warning_label = tk.Label(
        interrogation,
        text="  ВЫ НЕ СМОЖЕТЕ ВЫЙТИ ИЗ ДОПРОСА, ПОКА НЕ ДАДЕТЕ ОТВЕТ  ", 
        font=("Arial", 12, "bold"), 
        fg="#e74c3c", 
        bg='#2c3e50'
    )
    warning_label.place(relx=0.5, rely=0.95, anchor='center')



def calculator():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        selected = operations_listbox.curselection()
        if not selected:
            messagebox.showwarning("ОШИБКА", "ОПЕРАЦИЮ КТО ВЫБИРАТЬ БУДЕТ?? Я ЧТО ЛИ?")
            webbrowser.open_new_tab("https://yandex.ru/search/?text=операции+в+математике&lr=45&clid=11528186f")
            return
            
        operation = operations_listbox.get(selected[0])
        
        if operation == "Все операции бобика":
            
            results = []
            results.append(f"Сложение: {a} + {b} = {a + b}")
            results.append(f"Вычитание: {a} - {b} = {a - b}")
            results.append(f"Умножение: {a} × {b} = {a * b}")
            if b != 0:
                results.append(f"Деление: {a} ÷ {b} = {a / b:.2f}")
                print("ПОЛЬЗОВАТЕЛЬ МАКАН ДЕЛИТ НА НОЛЬ!!!")
            else:
                results.append("НЕВЕРНЫЙ СИНТАКСИС. НА 0 ДЕЛИТЬ НЕЛЬЗЯ.")
                
            
            result_label.config(text="\n".join(results))
        else:
            
            if operation == "Сложение бобика":
                result = a + b
            elif operation == "Вычитание бобика":
                result = a - b
            elif operation == "Умножение бобика":
                result = a * b
            elif operation == "Деление бобика":
                if b == 0:
                    messagebox.showerror("ОШИБКА!", "ВЫ ЧТО, МАКАН? ДЕЛИТЬ НА 0 НЕЛЬЗЯ!")
                    print("ПОЛЬЗОВАТЕЛЬ ДЕЛИТ НА 0!!!")
                    webbrowser.open_new_tab("https://yandex.ru/search/?clid=11528186&text=почему+нельзя+делить+на+0&l10n=ru&lr=45")
                    time.sleep(2)
                    messagebox.showerror("ВОСПИТАННОСТЬ БОБИКА", "ТЕПЕРЬ ПОНЯЛИ СВОЮ ОШИБКУ?")
                    
                    return
                result = a / b
            result_label.config(text=f"Результат бобика: {result}")
            
            if "1488.0" in result_label.cget("text"):
              ask1488 =  messagebox.askyesno("ТАК.", "ВЫ ЧТО СПЕЦИАЛЬНО СДЕЛАЛИ ОТВЕТ 1488, ИЛИ СОВПАДЕНИЕ?\n\nДА - ЕСЛИ СДЕЛАЛИ СПЕЦИАЛЬНО\n\nНЕТ - ЕСЛИ СОВПАДЕНИЕ")
                
            if ask1488:
                advanced_prison_1488()   
            else:
                messagebox.showinfo("СОВПАДЕНИЕ", "Ну ладно... надеюсь.")


                
    except ValueError:
        messagebox.showerror("ОШИБКА!", "ВЫ ЧТО МАКАН? Я ПУСТОТУ БУДУ СЧИТАТЬ??")
        time.sleep(1.5)
        messagebox.showwarning("ВНИМАНИЕ!", "ЕЩЕ РАЗ УВИЖУ ТАКОЕ, ПОВЕЗУ В МУРИНО НА 34089 ЭТАЖ!")
def advanced_prison_1488():
    
    
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    
    
    prison = tk.Toplevel()
    prison.title(" АДСКАЯ ТЮРЬМА ЗА 1488 (ТЮРЬМА №2 Г. МУРИНО) ")
    prison.attributes('-fullscreen', True) 
    prison.configure(bg='#000000')
    prison.attributes('-topmost', True)
    
    
    prison.protocol("WM_DELETE_WINDOW", lambda: None)
    prison.resizable(False, False)
    
    
    prison.bind('<F11>', lambda e: "break")
    prison.bind('<Escape>', lambda e: "break")
    
    sentence_time = 60
    start_time = time.time()
    
    
    main_frame = tk.Frame(prison, bg='#000000')
    main_frame.place(relx=0.5, rely=0.5, anchor='center')
    
    
    title_label = tk.Label(
        main_frame,
        text=" ВЫ ЗАКЛЮЧЕНЫ ЗА 1488! (ТЮРЬМА №2 Г. МУРИНО) ", 
        font=("Arial", 36, "bold"), 
        fg="red", 
        bg='#000000'
    )
    title_label.pack(pady=30)
    
    
    timer_label = tk.Label(
        main_frame,
        text=" Осталось: 60 секунд", 
        font=("Comic Sans MS", 28), 
        fg="yellow", 
        bg='#000000'
    )
    timer_label.pack(pady=20)
    
    
    progress_frame = tk.Frame(main_frame, bg='#000000')
    progress_frame.pack(pady=20)
    
    progress_bar = tk.Canvas(progress_frame, width=800, height=30, bg='#333333', highlightthickness=0)
    progress_bar.pack()
    progress_fill = progress_bar.create_rectangle(0, 0, 0, 30, fill='red', outline='')
    
    #
    quotes = [
        "«1488 - КАК НЕПРАВИЛЬНАЯ НОТА В СИМФОНИИ МАТЕМАТИКИ»",
        "«ЧИСЛА ДОЛЖНЫ ОБЪЕДИНЯТЬ, А НЕ РАЗДЕЛЯТЬ»",
        "«МАТЕМАТИКА - ЯЗЫК ВСЕЛЕННОЙ, ГОВОРИТЕ НА НЁМ КРАСИВО»",
        "«КАЖДОЕ ЧИСЛО ИМЕЕТ ДУШУ, КРОМЕ 1488»",
        "«ВЫ НАРУШИЛИ ГАРМОНИЮ ЧИСЛОВОГО КОСМОСА!»",
        "«60 СЕКУНД - МАЛОЕ НАКАЗАНИЕ ЗА БОЛЬШОЕ ПРЕСТУПЛЕНИЕ»",
        "«ДУМАЙТЕ О ЧИСЛАХ: π, e, φ, i... ОНИ ПРЕКРАСНЫ!»",
        "«МАТЕМАТИКА ПРОЩАЕТ, НО НЕ ЗАБЫВАЕТ...»",
        "«РИКРОЛЛ НА ФОНЕ - ЧАСТЬ ВАШЕГО НАКАЗАНИЯ!»",
        "«НАДЕЮСЬ, ВАМ НРАВИТСЯ МУЗЫКА НА ФОНЕ!»"
    ]
    
    quote_label = tk.Label(
        main_frame,
        text=quotes[0], 
        font=("Arial", 16, "italic"), 
        fg="#cccccc", 
        bg='#000000',
        wraplength=1000,
        justify="center"
    )
    quote_label.pack(pady=30)
    
    
    exit_button = tk.Button(
        main_frame,
        text="ЗАКЛЮЧЁН", 
        font=("Arial", 20, "bold"),
        bg="#8B0000", 
        fg="white",
        state="disabled",
        width=25,
        height=3,
        command=prison.destroy
    )
    exit_button.pack(pady=40)
    
    
    rickroll_label = tk.Label(
        prison,
        text=" На фоне играет рикролл (я вас зарикроллил хаа) ", 
        font=("Arial", 14), 
        fg="#00ff00", 
        bg='#000000'
    )
    rickroll_label.place(relx=0.5, rely=0.95, anchor='center')
    
    def update_prison():
        elapsed = time.time() - start_time
        remaining = max(0, sentence_time - elapsed)
        
        
        timer_label.config(text=f" Осталось: {int(remaining)} секунд")
        progress = (sentence_time - remaining) / sentence_time
        progress_bar.coords(progress_fill, 0, 0, 800 * progress, 30)
        
        
        quote_index = int(elapsed) % len(quotes)
        quote_label.config(text=quotes[quote_index])
        
        
        if int(elapsed) % 2 == 0:
            colors = ["yellow", "red", "green", "cyan", "magenta", "orange"]
            timer_label.config(fg=colors[int(elapsed) % len(colors)])
        
        if remaining <= 0:
            
            timer_label.config(text=" ВРЕМЯ ВЫШЛО! ВЫ СВОБОДНЫ!", fg="#00ff00")
            exit_button.config(state="normal", bg="#006400", text=" ВЫЙТИ НА СВОБОДУ!")
            quote_label.config(text="Надеюсь, этот урок запомнится надолго! Больше не вводите 1488!")
            rickroll_label.config(text=" Музыка остановилась! Вы свободны! ")
        else:
            prison.after(1000, update_prison)
    
    update_prison()


def max_messenger_check():
    
    check_window = tk.Toplevel()
    check_window.title("ПРОВЕРКА MAX")
    check_window.geometry("400x200")
    check_window.attributes('-topmost', True)
    
    tk.Label(check_window, text=" ВЫ УСТАНОВИЛИ МЕССЕНДЖЕР MAX?",font=("Arial", 14), wraplength=350).pack(pady=20)
    
    def yes_click():
        check_window.destroy()
        messagebox.showinfo(" ОТЛИЧНО!", "Спасибо за установку MAX!")
    
    def no_click():
        check_window.destroy()
        messagebox.showerror(" MAX НЕ УСТАНОВЛЕН!", "ОТПРАВЛЯЙТЕСЬ В ГОСДУМУ НА 45 СЕКУНД!")
        max_prison_45()
    
    btn_frame = tk.Frame(check_window)
    btn_frame.pack(pady=20)
    
    tk.Button(btn_frame, text="ДА!!!", command=yes_click, bg="green", fg="white", width=10).pack(side=tk.LEFT, padx=10)
    tk.Button(btn_frame, text="ЭЭЭ.... НЕТ...", command=no_click, bg="red", fg="white", width=10).pack(side=tk.LEFT, padx=10)


def max_prison_45():
    
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ") 
    
    max_prison = tk.Toplevel()
    max_prison.title(" ВЫ ЗАКЛЮЧЕНЫ В ГОСДУМЕ РФ!- ВЫ НЕ УСТАНОВИЛИ МЕССЕНДЖЕР! ")
    max_prison.attributes('-fullscreen', True)
    max_prison.configure(bg='#1a237e')  
    max_prison.attributes('-topmost', True)
    
    max_prison.protocol("WM_DELETE_WINDOW", lambda: None)
    max_prison.resizable(False, False)
    max_prison.bind('<F11>', lambda e: "break")
    max_prison.bind('<Escape>', lambda e: "break")
    
    sentence_time = 45 
    start_time = time.time()
    
    main_frame = tk.Frame(max_prison, bg='#1a237e')
    main_frame.place(relx=0.5, rely=0.5, anchor='center')
    
    title_label = tk.Label(
        main_frame,
        text=" ВЫ НЕ УСТАНОВИЛИ МЕССЕНДЖЕР MAX! ", 
        font=("comic sans MS", 32, "bold"), 
        fg="#ffd600",  
        bg='#1a237e'
    )
    title_label.pack(pady=30)
    
    timer_label = tk.Label(
        main_frame,
        text=" Осталось: 45 секунд", 
        font=("Arial", 24), 
        fg="#ffffff", 
        bg='#1a237e'
    )
    timer_label.pack(pady=20)
    
    progress_frame = tk.Frame(main_frame, bg='#1a237e')
    progress_frame.pack(pady=20)
    
    progress_bar = tk.Canvas(progress_frame, width=600, height=25, bg='#0d47a1', highlightthickness=0)
    progress_bar.pack()
    progress_fill = progress_bar.create_rectangle(0, 0, 0, 25, fill='#ffd600', outline='')
    
    max_messages = [
        " MAX - самый современный мессенджер!",
        " В MAX лучшие голосовые сообщения!",
        " MAX защищает вашу переписку!",
        " MAX работает быстрее всех!",
        " MAX имеет красивый интерфейс!",
        " Бесплатные звонки в MAX!",
        " MAX доступен по всему миру!",
        " MAX постоянно обновляется!"
    ]
    
    message_label = tk.Label(
        main_frame,
        text=max_messages[0], 
        font=("Arial", 14), 
        fg="#ffffff", 
        bg='#1a237e',
        wraplength=500,
        justify="center"
    )
    message_label.pack(pady=20)
    
    # СОЗДАЕМ ФРЕЙМ ДЛЯ КНОПОК
    button_frame = tk.Frame(main_frame, bg='#1a237e')
    button_frame.pack(pady=20)
    
    # КНОПКА "ВЫЙТИ И СКАЧАТЬ MAX"
    exit_button = tk.Button(
        button_frame,
        text="ВЫЙТИ И СКАЧАТЬ MAX", 
        font=("Arial", 14, "bold"),
        bg="#388e3c", 
        fg="white",
        state="disabled",
        width=18,
        height=2,
        command=max_prison.destroy
    )
    exit_button.pack(side=tk.LEFT, padx=10)
    
    # ИЗМЕНЕННАЯ ФУНКЦИЯ ОТКАЗА - ТЕПЕРЬ ВЕДЕТ НА ДОПРОС
    def refuse_and_punish():
        max_prison.destroy()
        messagebox.showwarning("ОТКАЗ ПРИНЯТ!", "ПЕРЕДАЕМ ВАС НА ДОПРОС!")
        time.sleep(2)
        max_interrogation()  
    
    refuse_button = tk.Button(
        button_frame,
        text="ОТКАЖУСЬ", 
        font=("Arial", 14, "bold"),
        bg="#d32f2f", 
        fg="white",
        state="disabled",
        width=15,
        height=2,
        command=refuse_and_punish  
    )
    refuse_button.pack(side=tk.LEFT, padx=10)
    
    def update_max_prison():
        elapsed = time.time() - start_time
        remaining = max(0, sentence_time - elapsed)
        
        timer_label.config(text=f" Осталось: {int(remaining)} секунд")
        progress = (sentence_time - remaining) / sentence_time
        progress_bar.coords(progress_fill, 0, 0, 600 * progress, 25)
        
        message_index = int(elapsed) % len(max_messages)
        message_label.config(text=max_messages[message_index])
        
        if remaining <= 0:
            timer_label.config(text=" ВРЕМЯ ВЫШЛО! УСТАНОВИТЕ MAX!", fg="#00ff00")
            exit_button.config(state="normal", bg="#388e3c")
            refuse_button.config(state="normal", bg="#d32f2f")
            message_label.config(text="Надеемся, вы установите MAX после выхода!")
        else:
            max_prison.after(1000, update_max_prison)
    
    update_max_prison()





window = tk.Tk()

window.title("Калькулятор Бобика Мурино")
window.geometry("350x800")




def schedule_random_max_check():
    check_delay = random.randint(10000, 60000)  
    window.after(check_delay, max_messenger_check)
schedule_random_max_check()




tk.Label(window, text="Первое число бобика:").pack()
entry1 = tk.Entry(window)
entry1.pack()

tk.Label(window, text="Второе число бобика:").pack()
entry2 = tk.Entry(window)
entry2.pack()


tk.Label(window, text="Выберите операцию бобика:").pack()

operations_listbox = tk.Listbox(window, height=5)
operations = ["Сложение бобика", "Вычитание бобика", "Умножение бобика", "Деление бобика", "Все операции бобика"]
for op in operations:
    operations_listbox.insert(tk.END, op)
operations_listbox.pack(pady=5)

def SHUTDOWN_COMP():
    Confirm1 = messagebox.askquestion("ПОДОЖДИТЕ...", "ВЫ УВЕРЕНЫ ЧТО ХОТИТЕ ВЫКЛЮЧИТЬ КОМПЬЮТЕР??")
    if Confirm1 == "yes":
        print("ОТПРАВЛЯЮ messagebox.showerror")
        messagebox.showerror("ВЫКЛЮЧАЮ ПК.", "ПРОЩАЙТЕ.")
        print("ВЫКЛЮЧАЮ КОМП")
        os.system("shutdown /s /t 300")
        time.sleep(3)
        print("ОТМЕНЯЮ ВЫКЛЮЧЕНИЕ КОМПА ЧЕРЕЗ ТАЙМЕР")
        os.system("shutdown /a")
        os.system("shutdown /a")
        print("shutdown /a")
        


    else:
        messagebox.showinfo("ВЫКЛЮЧЕНИЕ ПК ОТМЕНЕНО.", "ПРОДОЛЖАЙТЕ ТЕСТИРОВАТЬ ДОМАШНЕЕ ЗАДАНИЕ.")
        messagebox.showinfo("ЕСЛИ ЧТО", "КОМПЬЮТЕР НЕ БУДЕТ ВЫКЛЮЧЕН, ДАЖЕ ЕСЛИ НАЖАТЬ НА ДА")
def KodKoini():
    webbrowser.open_new_tab("https://erp.code-class.ru/admin/login")
def Murino():
    webbrowser.open_new_tab("https://ru.wikipedia.org/wiki/Мурино")
def Cs2():
    cs2_path = r"C:\Program Files (x86)\Steam\steam.exe"
    Cs2Confirm = messagebox.askquestion("Стоп.", "Вы уверены что хотите запустить прикольный шутер от первого лица вместо того чтобы проверять мое домашнее задание?")
    if Cs2Confirm == "yes":
        print("ЗАПУСКАЮ КС2...")
        if os.path.exists(cs2_path):
            os.system(f'"{cs2_path}" -applaunch 730')
            print("ИГРА БЫЛА УСПЕШНО ЗАПУЩЕНА. (ПОСТАВЬТЕ ПОЖАЛУЙСТА КОД КОИНЫ МАТВЕЮ А И МАКСИМУ Г)")

        else:
            messagebox.showerror("OS.SYSTEM ERROR", "ОШИБКА! КОД НЕ СМОГ ЗАПУСТИТЬ КС2!\n ПРИЧИНЫ:\n 1.У ВАС НЕ СКАЧАНО КС2(ЧТО ОЧЕНЬ СТРАННО, ПОСКОЛЬКУ ВЫ СМОТРИТЕ НОВОСТИ КС2)\n2. У ВАС НЕТУ СТИМА (ЧТО В ТРИЖДЫ СТРАННО)\n 3. ВЫ СПЕЦИАЛЬНО УДАЛИЛИ КС2 ПЕРЕД ПРОВЕРКОЙ ДОМАШКИ, ЧТОБЫ ДАЛЬШЕ ТЕСТИТЬ ДЗ!")
def Rolik():
   rolik2 = messagebox.askquestion("Внимание.", "Вы точно хотите перейти к видеоролику? (в браузере откроется ссылка)")
   if rolik2 == "yes":
       webbrowser.open_new_tab("https://t.me/c/3106726969/80")
def Krasniy():
    ask2 = messagebox.askquestion("Внимание.", "Вы уже красный и тд?")
    if ask2 == "yes":
        webbrowser.open_new_tab("https://drive.google.com/file/d/1Q-w0XtP0-ioP0u9zYyYdGsDZBFQWJsiE/view?usp=sharing")
    else:
        webbrowser.open_new_tab("https://drive.google.com/file/d/1MiLohC9c3dZc-Fp1PbKDNYJiHoHBbsrN/view?usp=sharing")
            

result_label = tk.Label(window, text="Результат Бобика: ", justify="left")
tk.Button(window, text="Где живет Максим", command=Murino, fg="green").pack(pady=15)
tk.Button(window, text="Вычислить Бобика", command=calculator).pack(pady=10)
tk.Button(window, text="ВЫКЛЮЧИТЬ КОМПЬЮТЕР☠️", command=SHUTDOWN_COMP, bg="#6b0707", fg="white").pack(pady=11)
tk.Label(window, text="------ ПОЛЕЗНЫЕ КНОПКИ ОЧЕНЬ ------", fg="#076b24", width=70).pack(pady=13)
tk.Button(window, text="Запустить Кс2 (если скучно проверять дз)", command=Cs2, bg="orange").pack(pady=17)
tk.Button(window, text="Начислить код коины (Рекомендуется)", command=KodKoini, bg="cyan", fg="black").pack(pady=18)
tk.Button(window, text="Посмотреть обучающий видеоролик", command=Rolik, bg="#8308ff", fg="#fbff08").pack(pady=18)
tk.Button(window, text="Я уже красный", command=Krasniy, bg="#b63131").pack(pady=18)
result_label.pack(pady=0)

window.mainloop()
def MINECRAFT():
    webbrowser.open_new_tab("https://drive.google.com/file/d/1grwi0VHUfbH4ByeM92cdJQak3ivFLReg/view?usp=sharing")


window2 = tk.Tk()
window2.title("МАЙНКР*ВТ")
window2.geometry("200x100")
MINECRFT = tk.Button(window2, text="ИГРАТЬ В МАЙНКР*ВТ",bg="green", command=MINECRAFT)
MINECRFT.pack(pady=0)
window2.mainloop()