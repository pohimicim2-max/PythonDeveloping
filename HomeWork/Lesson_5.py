Chisla = []
for i in range(10):
     chiverki = int(input("Число введи ток целое, а то бобик будет ругаться: "))
     Chisla.append(chiverki)

print(f"Отсортированный список бобика: {Chisla}")
print("*"*40)
 # Домашнее задание

text = "the quick brown fox jumps over the lazy dog."
# №1
NijniyText = text.lower()
# №2
BeZTochkiText = text.replace(".", "")
# №3
slova = BeZTochkiText.split()
# Метод split() в Python — это встроенный метод строк, который разделяет строку на подстроки по заданному разделителю.
# №4
DlinnieSlova = [slovo for slovo in slova if len(slovo) > 3]
# Длинные слова - слова которые больше трёх символов.
# №5
OchenDlinnoeSlovo = ""
for text in DlinnieSlova:
    if len(text) > len(OchenDlinnoeSlovo):
        OchenDlinnoeSlovo = text

print(f"Текст в нижнем регистре: {NijniyText}")
print(f"Текст без точек: {BeZTochkiText}")
print(f"Список бобика (Отредактированный, но не точно): {slova} ")
print(f"Слова бобика которые длиннее трёх символов: {DlinnieSlova}")
print(f"Очееееееееееееееееееееееееень длинное слово (Рекорд бобика): {OchenDlinnoeSlovo}")