# часть 1: Сумма чисел от 1 до n

while True:
    try:
        n = int(input("Введите положительное число: "))
        if n > 0:
            break
        else:
            print("Число должно быть больше 0!")
    except:
        print("Ошибка! Введите целое число.")

sum_result = 0

for number in range(1, n + 1):
    sum_result += number

print(f"Сумма чисел от 1 до {n} = {sum_result}")

print("=" * 50)

# часть 2: четные и нечетные числа

print("\nЧетные числа от 1 до 20:")

counter = 1

while counter <= 20:
    if counter % 2 == 0:
        print(counter)
    counter += 1

print("\nНечетные числа от 1 до 20:")

counter = 1

while counter <= 20:
    if counter % 2 != 0:
        print(counter)
    counter += 1

print("=" * 50)

# часть 3: дополнительно - красивое отображение

print("\nвсе числа от 1 до 20:")

for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i} (четное)")
    else:
        print(f"{i} (нечетное)")

print("\n" + "=" * 50)
print("Максим Мурино успешно завершил этот код")
print("=" * 50)