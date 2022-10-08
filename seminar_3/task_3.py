# Напишите программу, которая будет 
# преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input("Введите число: "))
num = number
binary_number = ""

for elem in range(number):
    binary_number = str(number % 2) + binary_number
    number = number // 2

print(f"- {num} -> {binary_number}")