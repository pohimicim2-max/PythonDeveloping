import data
import random
import os
import pygame
from plyer import notification
from tkinter import messagebox
import sys
import tkinter as tk
import time
import webbrowser
import threading

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

score = 0
quest_index = 0
current_questions = []
current_correct = ""
quiz_active = False
prison_triggered = False

downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
jail_image_path = os.path.join(downloads_path, "jail.png")

def send_warning():
    messagebox.showinfo("ВНИМАНИЕ", "В коде присутствуется музыка. Убавьте немного пожалуйста :)")

def init_quiz_by_difficulty(difficulty="ЛЕГКИЙ"):
    global score, quest_index, current_questions, current_correct, quiz_active
    
    if difficulty == "ВСЕ":
        all_questions = []
        for diff in data.questions.values():
            all_questions.extend(diff.copy())
        current_questions = all_questions
    elif difficulty in data.questions:
        current_questions = data.questions[difficulty].copy()
    else:
        current_questions = data.questions["ЛЕГКИЙ"].copy()
    
    random.shuffle(current_questions)
    score = 0
    quest_index = 0
    current_correct = ""
    quiz_active = True
    return True

def init_custom_quiz(questions_list):
    global score, quest_index, current_questions, current_correct, quiz_active
    current_questions = questions_list.copy()
    random.shuffle(current_questions)
    score = 0
    quest_index = 0
    current_correct = ""
    quiz_active = True
    return True

def get_random_questions(difficulty="ВСЕ", count=10):
    if difficulty == "ВСЕ":
        all_q = []
        for diff in data.questions.values():
            all_q.extend(diff.copy())
        selected = all_q
    elif difficulty in data.questions:
        selected = data.questions[difficulty].copy()
    else:
        selected = []
    
    random.shuffle(selected)
    return selected[:count] if count > 0 else selected

def get_mixed_random_questions(count=15):
    all_q = []
    for diff in data.questions.values():
        all_q.extend(diff.copy())
    random.shuffle(all_q)
    return all_q[:count] if count > 0 else all_q

def get_progressive_questions(count=12):
    difficulties = ["ЛЕГКИЙ", "СРЕДНИЙ", "СЛОЖНЫЙ", "ХАРДКОР ДЛЯ ДМИТРИЯ"]
    result = []
    
    for i, diff in enumerate(difficulties):
        if diff in data.questions:
            q_list = data.questions[diff].copy()
            random.shuffle(q_list)
            needed = max(1, count // len(difficulties))
            if i == len(difficulties) - 1:
                needed = max(1, count - len(result))
            result.extend(q_list[:needed])
    
    random.shuffle(result)
    return result[:count]

def generate_quest(QUEST, buttons, result_label=None):
    global quest_index, current_questions, current_correct, quiz_active
    
    if not quiz_active:
        if result_label:
            result_label.config(text="ВИКТОРИНА НЕ АКТИВНА", fg="red")
        return False
    
    if not current_questions:
        QUEST.config(text="НЕТ ВОПРОСОВ")
        if result_label:
            result_label.config(text="")
        return False
    
    if quest_index >= len(current_questions):
        print(f"\n{'='*50}")
        print(f"ВИКТОРИНА ЗАВЕРШЕНА! ФИНАЛЬНЫЙ СЧЁТ: {score}/{len(current_questions)}")
        print(f"{'='*50}")
        QUEST.config(text=f"ВИКТОРИНА ЗАВЕРШЕНА! СЧЁТ: {score}/{len(current_questions)}")
        for btn in buttons:
            btn.config(state="disabled")
        if result_label:
            result_label.config(text="НАЖМИТЕ 'РЕСТАРТ' ДЛЯ НОВОЙ ИГРЫ", fg="yellow")
        quiz_active = False
        return False
    
    current = current_questions[quest_index]
    QUEST.config(text=current["quest"])
    current_correct = current["right"]
    
    print(f"\n{'='*50}")
    print(f"{Colors.GREEN}ВОПРОС {quest_index + 1}/{len(current_questions)}")
    print(f"ТЕКУЩИЙ СЧЁТ: {score}")
    print(f"{'='*50}")
    print(f"ВОПРОС: {current['quest']}")
    print(f"ПРАВИЛЬНЫЙ ОТВЕТ: НЕ СКАЖУ!{Colors.RESET}")
    
    answers = current["answers"].copy()
    random.shuffle(answers)
    
    print("ВАРИАНТЫ:")
    for i, ans in enumerate(answers):
        print(f"  {i+1}. {ans}")
    print(f"{'='*50}")
    
    for i, btn in enumerate(buttons):
        if i < len(answers):
            btn.config(text=answers[i], state="normal")
        else:
            btn.config(text="", state="disabled")
    
    if result_label:
        result_label.config(text="")
    
    return True

def check_answer(selected_index, QUEST, buttons, result_label=None, score_label=None):
    global score, quest_index, current_correct, quiz_active
    
    if not quiz_active or quest_index >= len(current_questions):
        return False
    
    selected_text = buttons[selected_index]["text"]
    
    print(f"\n► ВЫБРАН ОТВЕТ: {selected_text}")
    print(f"► ПРАВИЛЬНЫЙ: {current_correct}")
    
    if selected_text == current_correct:
        score += 1
        print(f" ПРАВИЛЬНО! Текущий счёт: {score}")
        if result_label:
            result_label.config(text=" ПРАВИЛЬНО!", fg="green")
        if score_label:
            score_label.config(text=f"ОТЛИЧНО! +1", fg="green")
            QUEST.after(1500, lambda: score_label.config(text=f"Счёт: {score}"))
    else:
        print(f" ОШИБКА! Текущий счёт: {score}")
        if result_label:
            result_label.config(text=f" НЕПРАВИЛЬНО! Правильно: {current_correct}", fg="red")
        if score_label:
            score_label.config(text="ПЛОХО! 0", fg="red")
            QUEST.after(1500, lambda: score_label.config(text=f"Счёт: {score}"))
    
    quest_index += 1
    
    if quest_index < len(current_questions):
        generate_quest(QUEST, buttons, result_label)
    else:
        print(f"\n{'='*50}")
        print(f" ВИКТОРИНА ЗАВЕРШЕНА!")
        print(f"ФИНАЛЬНЫЙ СЧЁТ: {score}/{len(current_questions)}")
        print(f"ПРОЦЕНТ ПРАВИЛЬНЫХ: {int(score/len(current_questions)*100)}%")
        print(f"{'='*50}")
        
        QUEST.config(text=f"КОНЕЦ! СЧЁТ: {score}/{len(current_questions)}")
        for btn in buttons:
            btn.config(state="disabled")
        if result_label:
            result_label.config(text="ВИКТОРИНА ЗАВЕРШЕНА", fg="green")
        quiz_active = False
    
    return True

def restart_quiz():
    global score, quest_index, quiz_active
    score = 0
    quest_index = 0
    quiz_active = True
    return True

def get_score():
    return score

def get_total_questions():
    return len(current_questions) if current_questions else 0

def get_current_question_num():
    return quest_index + 1 if quest_index < len(current_questions) else len(current_questions)

def is_quiz_active():
    return quiz_active

def is_quiz_finished():
    return not quiz_active or quest_index >= len(current_questions)

def send_goodluck():
    notification.notify(
    title="Совет",
    message="Удачи.",
    timeout=1,
    toast=True
)

def advanced_prison_1488(root_window=None):
    global prison_triggered
    
    if prison_triggered:
        return
    
    prison_triggered = True
    
    try:
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    except:
        pass
    
    if root_window is None:
        root_window = tk.Tk()
        root_window.withdraw()
    
    prison = tk.Toplevel(root_window)
    prison.title("АДСКАЯ ТЮРЬМА ЗА ПЛОХОЙ РЕЗУЛЬТАТ")
    prison.attributes('-fullscreen', True)
    prison.configure(bg='#000000')
    prison.attributes('-topmost', True)
    
    prison.protocol("WM_DELETE_WINDOW", lambda: None)
    prison.resizable(False, False)
    
    prison.bind('<F11>', lambda e: "break")
    prison.bind('<Escape>', lambda e: "break")
    
    sentence_time = 10
    start_time = time.time()
    
    main_frame = tk.Frame(prison, bg='#000000')
    main_frame.place(relx=0.5, rely=0.5, anchor='center')
    
    title_label = tk.Label(
        main_frame,
        text="ВЫ НЕ ЗНАЕТЕ ИДЕАЛЬНО ПАЙТОН!",
        font=("Arial", 36, "bold"),
        fg="red",
        bg='#000000'
    )
    title_label.pack(pady=30)
    
    timer_label = tk.Label(
        main_frame,
        text=f"Осталось: {sentence_time} секунд",
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
    
    quotes = [
        "МАКСИМ ЖДЕТ, ПОКА ВЫ ПОСМОТРИТЕ ЕГО КОД!",
        "ПЛОХОЙ РЕЗУЛЬТАТ = ТЮРЬМА!",
        "148 СЕКУНД РАЗМЫШЛЕНИЙ О СВОИХ ОШИБКАХ",
        "РИКРОЛЛ - ЛУЧШЕЕ НАКАЗАНИЕ!",
        "НАДЕЮСЬ, ВАМ НРАВИТСЯ МУЗЫКА!",
        "ВЫ ЗАСЛУЖИЛИ ЭТО!",
        "ПОДУМАЙТЕ О СВОЁМ ПОВЕДЕНИИ!",
        "СЛЕДУЮЩИЙ РАЗ УЧИТЕ ПАЙТОН ЛУЧШЕ!"
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
        text="На фоне играет рикролл (я вас зарикроллил хаа)",
        font=("Arial", 14),
        fg="#00ff00",
        bg='#000000'
    )
    rickroll_label.place(relx=0.5, rely=0.95, anchor='center')
    
    def update_prison():
        elapsed = time.time() - start_time
        remaining = max(0, sentence_time - elapsed)
        
        timer_label.config(text=f"Осталось: {int(remaining)} секунд")
        progress = (sentence_time - remaining) / sentence_time
        progress_bar.coords(progress_fill, 0, 0, 800 * progress, 30)
        
        quote_index = int(elapsed) % len(quotes)
        quote_label.config(text=quotes[quote_index])
        
        if int(elapsed) % 2 == 0:
            colors = ["yellow", "red", "green", "cyan", "magenta", "orange"]
            timer_label.config(fg=colors[int(elapsed) % len(colors)])
        
        if remaining <= 0:
            timer_label.config(text="ВРЕМЯ ВЫШЛО! ВЫ СВОБОДНЫ!", fg="#00ff00")
            exit_button.config(state="normal", bg="#006400", text="ВЫЙТИ НА СВОБОДУ!")
            quote_label.config(text="Надеюсь, этот урок запомнится надолго!")
            rickroll_label.config(text="Музыка остановилась! Вы свободны!")
        else:
            prison.after(1000, update_prison)
    
    update_prison()
    return prison

def fake_console_error_trap(root_window):
    if hasattr(fake_console_error_trap, 'already_called'):
        return
    fake_console_error_trap.already_called = True
    
    print(f"\n{'='*80}")
    print(f"{Colors.RED}ERROR: Critical failure in quiz evaluation module{Colors.RESET}")
    print(f"{'='*80}")
    
    error_lines = [
        "Traceback (most recent call last):",
        '  File "c:\\Users\\Qkrt\\OneDrive\\Документы\\GitHub\\PythonDeveloping\\lesson10\\main.py", line 147, in end_quiz',
        '    percentage = (funcs.get_score() / funcs.get_total_questions()) * 100',
        "ZeroDivisionError: division by zero",
        "",
        "During handling of the above exception, another exception occurred:",
        "",
        "Traceback (most recent call last):",
        '  File "c:\\Users\\Qkrt\\OneDrive\\Документы\\GitHub\\PythonDeveloping\\lesson10\\main.py", line 153, in <lambda>',
        '    mainWindow.after(2000, lambda: funcs.advanced_prison_1488(mainWindow))',
        "MemoryError: Cannot allocate 1488 bytes in protected memory",
        "",
        "Stack dump:",
        "0x7FF8A1B3C4D0: quiz_core::evaluate()",
        "0x7FF8A1B3C5A0: tkinter_callback_dispatcher()",
        "0x7FF8A1B3C670: python_internal_error_handler()",
        "HEAP CORRUPTION DETECTED at 0x000001B14881488",
        "CRITICAL: PYTHON INTERPRETER IS UNSTABLE",
        "",
        f"{Colors.YELLOW}Recommended action: Restart application and check quiz logic{Colors.RESET}",
        f"{Colors.CYAN}Press Ctrl+C to abort... (just kidding, it won't help){Colors.RESET}",
        f"{'='*80}"
    ]
    
    def print_slowly():
        for line in error_lines:
            print(line)
            time.sleep(0.3)
        
        time.sleep(1)
        print(f"\n{Colors.RED}Attempting to recover...{Colors.RESET}")
        time.sleep(1)
        print(f"{Colors.YELLOW}Recovery failed. Memory allocation error 0x1488{Colors.RESET}")
        time.sleep(1)
        print(f"{Colors.RED}Switching to emergency protocol 'PRISON_MODE'{Colors.RESET}")
        time.sleep(1)
        print(f"{Colors.CYAN}Initializing punitive measures in 3...{Colors.RESET}")
        sys.stdout.flush()
    
    error_thread = threading.Thread(target=print_slowly)
    error_thread.daemon = True
    error_thread.start()
    
    root_window.after(4000, lambda: advanced_prison_1488(root_window))