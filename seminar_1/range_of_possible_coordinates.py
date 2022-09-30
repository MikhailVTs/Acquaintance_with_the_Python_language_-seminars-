# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти 
# (x и y).

print()

quarter = int(input("Ввведите номер четверти (1, 2, 3 или 4): "))

print()

if quarter != 0 and quarter <= 4:
    if quarter == 1:
        print(f"- {quarter} четверть -> x > 0 and y > 0")
    elif quarter == 2:
        print(f"- {quarter} четверть -> x < 0 and y > 0")
    elif quarter == 3:
        print(f"- {quarter} четверть -> x < 0 and y < 0")
    else:
        print(f"- {quarter} четверть -> x > 0 and y < 0")
else:
    print("Будьте внимательны, перечитайте задание!!!")