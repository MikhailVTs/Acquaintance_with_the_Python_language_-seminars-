# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
list_numbers = []
list_numbers_odd_pos = []

number = int(input("Введите число: "))

sum_numbers = 0

for elem in range(number):
    list_numbers.append(random.randint(1, 101))


for elem_pos in range(len(list_numbers)):
    if elem_pos % 2 != 0:
        sum_numbers += list_numbers[elem_pos]
        list_numbers_odd_pos.append(list_numbers[elem_pos])
       
print(f"- {list_numbers} -> на нечётных позициях элементы {str(list_numbers_odd_pos)[1:-1]}, ответ: {sum_numbers}")