from random import shuffle

candies = 2021
max_number_of_candies = 28

game_conditions = '''Условия Игры: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
        Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
        Все конфеты оппонента достаются сделавшему последний ход.
        Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?'''

print()
print(game_conditions)
print()

name_1 = input("Введите своё имя: ")
name_2 = "Конфетоед"
print()
print(f"{name_1} с Вами будет играть бот по имени {name_2}")

def bot_run(candies: int):
    if candies <= max_number_of_candies:
        result = candies
    else:
        result = max_number_of_candies
        cnt_step = candies // max_number_of_candies
        if candies % max_number_of_candies > 0:
            cnt_step += 1
        if cnt_step % 2 == 0:
            if candies - max_number_of_candies < max_number_of_candies:
                result = candies - (max_number_of_candies - 1)
    return result

rest_candies = candies

players = [name_1, name_2]
shuffle(players)

active_player = players[0]

print()
print(f"И так!!! Первым начнёт игру под именем - {players[0]}, ну и вторым кто будет начинать игру зовут - {players[1]}")
print()
print(f"НАЧИНАЕМ ИГРУ!!!")
print()

while rest_candies > 0:

    print(f"Передвами {rest_candies} конфета, у Вас есть возвожность выбора взять 1 конфету или же {max_number_of_candies} конфет (это максимум конфет который вы можете взять за один раз)")
    print()
    print(f"Игрок под именем {active_player} начинает ход")

    if active_player == name_2:
         get_candies = bot_run(rest_candies)
         print(f"{name_2} взял {get_candies} конфет")
         print()
    else:
        get_candies = int(input(f"Сколько конфеты ты хочешь взять {active_player} ? "))
        print()
    if get_candies not in range(1, max_number_of_candies + 1):
        print("Подумай лучше, сколько ты конфет можешь взять!")
    else:
        rest_candies -= get_candies
        if rest_candies > 0:
            active_player = name_1 if active_player == name_2 else name_2
        else:
            print()
            print(f"Игрко под именем {active_player} ПОБЕДИЛ!")