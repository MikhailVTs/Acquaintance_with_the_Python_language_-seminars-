# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной 
# последовательности.

from random import randint


list_numbers = []

for elem in range(10):
    list_numbers.append(randint(1, 11))

print(list_numbers)

print(set(list_numbers))

