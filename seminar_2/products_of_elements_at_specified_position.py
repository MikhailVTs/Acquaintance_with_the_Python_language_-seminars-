# Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, 
# заполненных чмслами из прмежутка [-N, N]. Найдите произведение элементов на указанных 
# позициях (не индексах).

# Пример:

# Position one: 1
# Position two: 3
# Number of elements: 5
# ->[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5] 
# ->15



print()
pos_elm_one = int(input("Введите число для первой позиции: "))
pos_elm_two = int(input("Введите число для второй позиции: "))
print()
num_of_elm = int(input("Введите количество элементов: "))
print()

list = []

for i in range(-num_of_elm, num_of_elm +1):
    list.append(i)


print(f"->{list}")

multipl_elem = list[pos_elm_one-1] * list[pos_elm_two-1]

print(f"->{multipl_elem}")