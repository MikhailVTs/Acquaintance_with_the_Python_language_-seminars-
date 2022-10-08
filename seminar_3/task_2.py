# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем 
# первой и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
import numpy as np

list_numbers = []

number = int(input("Введите число: "))

for elem in range(number):
    list_numbers.append(random.randint(1, 101))

length = len(list_numbers)

if length % 2 == 0:

    index = length // 2

    left_list = list_numbers[:index]
    right_list = list_numbers[index:]
    right_list_rev = right_list.reverse()
    
    print(f"- {list_numbers} => {np.multiply(left_list, right_list)}")

else:
    
    index = length // 2

    left_list = list_numbers[:index+1]
    right_list = list_numbers[index:]
    right_list_rev = right_list.reverse()
    
    print(f"- {list_numbers} => {np.multiply(left_list, right_list)}")