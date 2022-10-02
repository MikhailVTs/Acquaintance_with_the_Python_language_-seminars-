# Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.

# Пример:

# 10
# ->[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# ->[0, 7, 6, 3, 4, 2, 9, 5, 1, 8]
import random

list = []
print()
number = int(input("Введите число: "))
print()
for i in range(number):
    list.append(i)

print(f"-> {list}")
print()
for i in range(len(list)):
    index = random.randint(0, len(list)-1)
    tmp = list[i]
    list[i] = list[index]
    list[index] = tmp

print(f"-> {list}")