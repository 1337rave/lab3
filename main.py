
# Зчитуємо число з клавіатури
number = int(input("Введіть число: "))

# Перевіряємо, чи є число парним чи непарним
if number % 2 == 0:
    print(f"{number} - Even number")
else:
    print(f"{number} - Odd number")

