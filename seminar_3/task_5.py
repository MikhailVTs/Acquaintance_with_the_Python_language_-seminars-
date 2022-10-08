# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.

# Пример:
# - 8 -> -21, 13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21
# - 3 -> 2, -1, 1, 0, 1, 1, 2 

number = int(input("Введите число: "))

list_fibonacci = []

fibonacci_1 = 0
fibonacci_2 = 1

list_fibonacci_minus = [fibonacci_1, fibonacci_2]

for elem in range(2, number+1):
    fibonacci_1, fibonacci_2 = fibonacci_2, fibonacci_1 - fibonacci_2
    list_fibonacci_minus.append(fibonacci_2)



fibonacci_1 = 1
fibonacci_2 = 1

list_fibonacci_a_plus = [fibonacci_1, fibonacci_2]
for elem in range(2, number):
    fibonacci_1, fibonacci_2 = fibonacci_2, fibonacci_1 + fibonacci_2
    list_fibonacci_a_plus.append(fibonacci_2)

list_fibonacci_minus_rev = list_fibonacci_minus[::-1]

list_fibonacci = list_fibonacci_minus_rev + list_fibonacci_a_plus   
print(f" - {number} -> {str(list_fibonacci)[1:-1]}")