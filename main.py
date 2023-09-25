operation = input("Виберіть операцію (+ для додавання, - для віднімання, * для множення): ")
number1 = float(input("Введіть перше число: "))
number2 = float(input("Введіть друге число: "))
if operation == '+':
    result = number1 + number2
    print(f"Сума {number1} і {number2} дорівнює {result}")
elif operation == '-':
    result = number1 - number2
    print(f"Різниця {number1} і {number2} дорівнює {result}")
elif operation == '*':
    result = number1 * number2
    print(f"Добуток {number1} і {number2} дорівнює {result}")
else:
    print("Невідома операція. Будь ласка, виберіть +, - або *.")

