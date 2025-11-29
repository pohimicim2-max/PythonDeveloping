chislo1 = int(input("Введи число "))
chislo2 = 0
for i in range(1, chislo1 + 1):
    chislo2 += i

print(f"Cумма чисел от 1 до {chislo1} = {chislo2}")
# --------------------------------------------------------------
# 2-я задача

chislo = 1
print("Четные")
while i <= 20:
    if i % 2 == 0:
        print(chislo)
    i += 1

print("Нечетные")
while i <= 20:
    if i % 2 != 0:
        print(chislo)
    i += 1