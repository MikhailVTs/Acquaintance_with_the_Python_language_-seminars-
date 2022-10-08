# задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением 
# дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

list_numbers = []
list_float_numbers = []
count_num = int(input("Введите количестов чисел: "))
for rand_num_float in range(count_num):
    list_numbers.append(round(random.uniform(1, 101), 2))

for elem in list_numbers:
    if isinstance(elem, float):
        list_float_numbers.append(elem % 1)

number = max(list_float_numbers) - min(list_float_numbers)

print(f"- {list_numbers} => {number:.2f}")