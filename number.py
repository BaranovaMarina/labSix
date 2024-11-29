def count_vowels_in_text():
    # Введення тексту користувачем
    text = input("Введіть текст, що містить цифри та літери латинського алфавіту: ")

    # Множина голосних літер
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}

    # Рахуємо кількість голосних літер (незалежно від регістру)
    count = sum(1 for char in text.lower() if char in vowels)

    # Вивід результату
    print(f"Кількість голосних літер у тексті: {count}")


# Виклик функції
count_vowels_in_text()