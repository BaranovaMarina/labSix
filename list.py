def split_list():
    # Введення списку користувачем
    user_input = input("Введіть елементи списку через пробіл (літери та цифри): ")

    # Розділяємо введення на елементи списку
    elements = user_input.split()

    # Ініціалізуємо списки для цифр і літер
    digits = []
    letters = []

    # Розділяємо елементи на цифри та літери
    for element in elements:
        if element.isdigit():
            digits.append(int(element))  # Перетворюємо цифри у числовий тип
        elif element.isalpha():
            letters.append(element)
        else:
            print(f"Ігнорується некоректний елемент: {element}")

    # Друк результатів
    print("Список цифр:", digits)
    print("Список літер:", letters)


# Виклик функції
split_list()
