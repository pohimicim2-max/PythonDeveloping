
import datetime


current_year = datetime.datetime.now().year


name = input("Введите ваше имя: ")


while True:
    try:
        birth_year = int(input("Введите ваш год рождения: "))
        
        if 1900 <= birth_year <= current_year:
            break
        else:
            print(f"пожалуйста, введите год между 1900 и {current_year}")
    except ValueError:
        print("ошибка! введите целое число для года рождения")


hobby = input("Введите ваше хобби: ")


age = current_year - birth_year

print("\n" + "*" * 40)
print(f"добрый день, {name}")
print(f"вам: {age} лет.")
print(f"ваше любимое хобби: {hobby}")
print("*" * 40)

print("\n" + "-" * 40)
print("дополнительная информация:")
print(f"текущий год: {current_year}")
print(f"вы родились в {birth_year} году")

# проверка на совершеннолетие
if age >= 18:
    print("вы совершеннолетний, Вы получите повестку на портале Госуслуги.")
else:
    print("вы несовершеннолетний")

