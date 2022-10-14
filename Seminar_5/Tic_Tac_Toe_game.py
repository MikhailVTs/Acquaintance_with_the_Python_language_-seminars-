# import pyfiglet

# result = pyfiglet.figlet_format("Tic Tac Toe", font="slant")
# print(result)

text_game = """Кре́стики-но́лики — логическая игра между двумя противниками
            на квадратном поле 3 на 3 клетки или бо́льшего размера. Один
            из игроков играет «крестиками», второй — «ноликами»."""

print()
print(text_game)
print()
print()

birdcage = [i for i in range(1, 10)]

def riuse_cage(birdcage):
    print("#" * 13)
    for i in range(3):
        print(" ", birdcage[0 + i * 3], "#", birdcage[1 + i * 3], "#", birdcage[2 + i * 3], " ")
        print("#" * 13)
    print()


def take_input(x_or_y):
    validation = False
    while not validation:
        player_turn = input(f"Игрок {x_or_y} выбери клетку: ")
        print()
        try:
            player_turn = int(player_turn)
        except:
            print("Не торопись! Посмотри куда нажал")
            continue
        if player_turn >= 1 and player_turn <= 9:
            if (str(birdcage[player_turn - 1]) not in "XO"):
                birdcage[player_turn - 1] = x_or_y
                validation = True
            else:
                print("Будь внимателен!")
        else:
            print("Будь внимателен! Введите число от 1 до 9.")

def victory_conditions(birdcage):
    victory_positions = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for positions in victory_positions:
        if birdcage[positions[0]] == birdcage[positions[1]] == birdcage[positions[2]]:
            return birdcage[positions[0]]
    return False

def main(birdcage):
    counter = 0
    victory = False
    while not victory:
        riuse_cage(birdcage)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            player = victory_conditions(birdcage)
            if player:
                print(f"{player} Выиграл!")
                print("\U0001f61b")
                print()
                victory = True
        if counter == 9:
            print("Равные силы!")
main(birdcage)
