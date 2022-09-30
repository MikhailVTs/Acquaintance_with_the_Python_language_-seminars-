# Напишите программу, которая принимает на вход 
# координаты двух точек и находит расстояние между 
# ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math

print()
print("Введите координтаты:")
print()
print("1. Координаты точки A: ")
print()

xa = int(input("  a) Точка xa: "))
ya = int(input("  b) Точка ya: "))

print()
print("2. Координаты точки B: ")
print()

xb = int(input("  a) Точка xb: "))
yb = int(input("  b) Точка yb: "))

distance = math.sqrt(pow((xa - xb),2) + pow((ya - yb),2))

print()
print(f"- A ({xa}, {ya}); B ({xb}, {yb}) -> {distance:.2f}")