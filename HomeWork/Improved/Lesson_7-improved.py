
def rectangle_info(length, width):

    perimeter = 2 * (length + width)
    area = length * width
    diagonal = (length**2 + width**2)**0.5
    
    print("\n" + "="*50)
    print(" ПАРАМЕТРЫ ПРЯМОУГОЛЬНИКА")
    print("="*50)
    print(f" Длина: {length}")
    print(f" Ширина: {width}")
    print(f" Периметр: {perimeter:.2f}")
    print(f" Площадь: {area:.2f}")
    print(f" Диагональ: {diagonal:.2f}")
    
    if length == width:
        print(" Это квадрат Максима!")
    print("="*50)
    
    return perimeter, area, diagonal


def fibonacci_sequence(n):

    if n <= 0:
        print("Ошибка: n должно быть положительным числом!")
        return []
    
    sequence = []
    
    if n >= 1:
        sequence.append(0)
    if n >= 2:
        sequence.append(1)
    
    for i in range(2, n):
        next_number = sequence[i-1] + sequence[i-2]
        sequence.append(next_number)
    
    return sequence


def print_fibonacci_info(sequence, n):
    
    if not sequence:
        return
    
    print("\n" + "="*50)
    print("🌀 ПОСЛЕДОВАТЕЛЬНОСТЬ ФИБОНАЧЧИ")
    print("="*50)
    
    print(f"🔢 Первые {n} чисел:")
    
   
    for i in range(0, len(sequence), 10):
        chunk = sequence[i:i+10]
        print("   " + " ".join(f"{num:>4}" for num in chunk))
    
    print(f"\n📈 Статистика:")
    print(f"   Количество чисел: {len(sequence)}")
    print(f"   Сумма: {sum(sequence)}")
    
    if len(sequence) >= 2:
        last_ratio = sequence[-1] / sequence[-2]
        print(f"   Отношение последних: {last_ratio:.6f}")
    
    
    max_number = max(sequence) if sequence else 0
    print(f"   Максимальное число: {max_number}")
    
    print("="*50)


def golden_ratio_approximation(n):
    
    if n < 3:
        return None
    
    sequence = fibonacci_sequence(n)
    if len(sequence) < 2 or sequence[-2] == 0:
        return None
    
    return sequence[-1] / sequence[-2]



def main():
    print("="*60)
    print("🧮 МАТЕМАТИЧЕСКИЕ РАСЧЕТЫ")
    print("="*60)
    
    # Часть 1: Прямоугольник
    print("\n" + ""*20)
    print("ЧАСТЬ 1: ПРЯМОУГОЛЬНИК")
    print("📐"*20)
    
    print("\n Пример 1: прямоугольник")
    rectangle_info(5, 8)
    
    print("\n пример 2: квадрат 7×7")
    rectangle_info(7, 7)
    
    # часть 2: числа Фибоначчи
    print("\n" + ""*20)
    print("ЧАСТЬ 2: ЧИСЛА ФИБОНАЧЧИ")
    print(""*20)
    
    # Несколько примеров
    test_numbers = [10, 15, 20]
    
    for n in test_numbers:
        sequence = fibonacci_sequence(n)
        print_fibonacci_info(sequence, n)
        
        if len(sequence) >= 3:
            golden_approx = golden_ratio_approximation(n)
            true_golden = 1.618033988749895
            if golden_approx:
                print(f"   Приближение φ: {golden_approx:.8f}")
                print(f"   Истинное φ:    {true_golden:.8f}")
                error = abs(true_golden - golden_approx)
                print(f"   Погрешность:   {error:.8f}")
                print()
    
    # Часть 3: п ользовательский ввод
    print("\n" + ""*20)
    print("ЧАСТЬ 3: ВАШИ РАСЧЕТЫ")
    print(""*20)
    
    try:
        user_length = float(input("\nВведите длину прямоугольника: "))
        user_width = float(input("Введите ширину прямоугольника: "))
        rectangle_info(user_length, user_width)
        
        user_n = int(input("\nСколько чисел Фибоначчи вывести? "))
        user_sequence = fibonacci_sequence(user_n)
        print_fibonacci_info(user_sequence, user_n)
        
    except ValueError as oshibka:
        print(f"Ошибка ввода.Ошибка: {oshibka}")

main()