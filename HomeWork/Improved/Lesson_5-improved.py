numbers = []

for count in range(10):
    while True:
        try:
            number = int(input(f"Введите целое число #{count + 1}: "))
            numbers.append(number)
            break
        except ValueError:
            print("Ошибка! Нужно ввести целое число.")

print(f"\nСортированный список: {sorted(numbers)}")
print("*" * 40)

text = "the quick brown fox jumps over the lazy dog."

lower_text = text.lower()
text_without_dots = lower_text.replace(".", "")
words = text_without_dots.split()
long_words = [word for word in words if len(word) > 3]

longest_word = ""
for word in long_words:
    if len(word) > len(longest_word):
        longest_word = word

print(f"Текст в нижнем регистре: {lower_text}")
print(f"Текст без точки: {text_without_dots}")
print(f"Список слов: {words}")
print(f"Слова длиннее 3 символов: {long_words}")

if longest_word:
    print(f"Самое длинное слово: '{longest_word}' (длина: {len(longest_word)})")
else:
    print("Нет слов длиннее 3 символов")

print("*" * 40)

print("\nДополнительная информация:")
print(f"Всего слов: {len(words)}")
print(f"Длинных слов: {len(long_words)}")

if words:
    average_length = sum(len(word) for word in words) / len(words)
    print(f"Средняя длина слова: {average_length:.1f} символов")

print("\nРаспределение по длине слов:")
for length in range(1, 11):
    words_with_length = [word for word in words if len(word) == length]
    if words_with_length:
        print(f"  {length} символов: {len(words_with_length)} слов")