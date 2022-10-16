

def list_name_lastname():
    list_name = []
    list_lastname = []
    list_name_lastname = []
    num_people = int(input("Колличество людей, которые вы хотите внести в список: "))
    for num in range(num_people):
        name = input("Введите имя ")
        list_name.append(name)
        lastname = input("Введите фамилию ")
        list_lastname.append(lastname)
    list_name_lastname = zip(list_name, list_lastname)

    dict = {'Имя и фамилия': list(map(lambda u: {'Имя': u[0], 'Фамилия': u[1]}, list_name_lastname))}
    print(dict)

def main():
    list_name_lastname()


if __name__ == '__main__':
    main()

