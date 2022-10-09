# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

import math

number = int(input("Введите число: "))

list_number = []

while number % 2 == 0:
    list_number.append(2)
    number = number / 2

for i in range(3, int(math.sqrt(number)) +1, 2):
    while (number % i == 0):
        list_number.append(i)
        number = number / i
if number > 2:
    list_number.append(number)

print(list_number)
