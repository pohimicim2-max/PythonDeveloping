
current_year = 2025
name = input("Введите ваше имя: ")
birth_year = int(input("Введите ваш год рождения: "))
hobby = input("Введите ваше хобби: ")

age = current_year-birth_year


print("\n" + "*" * 40)
print(f"Добрый день, {name}")
print(f"Вам: {age} лет.")
print(f"Ваше любимое хобби: {hobby}")
print("*" * 40)
