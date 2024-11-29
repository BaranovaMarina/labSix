def replace_negative_with_zero():
    # Введення списку користувачем
    user_input = input("Введіть елементи списку через пробіл (цілі або дійсні числа): ")

    # Перетворюємо введені дані в список чисел
    try:
        numbers = [float(x) for x in user_input.split()]
    except ValueError:
        print("Будь ласка, введіть тільки числа.")
        return

    # Замінюємо всі від’ємні елементи на 0
    modified_list = [0 if num < 0 else num for num in numbers]

    # Виводимо результат
    print("Список після заміни від’ємних елементів на 0:")
    print(modified_list)


# Виклик функції
replace_negative_with_zero()
