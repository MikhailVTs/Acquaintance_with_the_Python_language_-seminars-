def dictionary_name(): 
    dictionary = {}
    num_name = int(input("Колличество имён, которые вы хотите внести в словарь: "))
    for name in range(num_name):
        name = input("Введите имя: ")
        try:
            dictionary[str(name[0])].append(name)
        except KeyError:
            dictionary[str(name[0])] = [name]
    print(dictionary)


def main():
    dictionary_name()

if __name__ == '__main__':
    main()


