import csv
import json


def menu():
    while True:
        print()
        print('\t Меню')

        print("Для выбора Вам необходимо ввести цифру от 1 до 8")
        print(f"1 Просмотреть все контакты")
        print(f"2 Найти контакт")
        print(f"3 Добавить контакт")
        print(f"4 Удалить контакт")
        print(f"5 Удалить все контакты")
        print(f"6 Сохранить телефонную книгу")
        print(f"7 Загрузить телефонную книгу")
        print(f"8 Закрыть телефонную книгу")

        number = input("Выберите действие: ")
        print()
        if number == "1":
            view_all_contacts()
        if number == "2":
            find_a_contact()
        if number == "3":
            add_contact()
        if number == "4":
            delete_contact()
        if number == "5":
            delete_all_contacts()
        if number == "6":
            save_phone_book()
        if number == "7":
            load_phone_book()
        if number == "8":
            break

def save_phone_book():

    print("Выберите формат для сохранения фаила")
    print("    1 - csv")
    print("    2 - json")
    print("    3 - txt")

    number_save = input("Что Вы выбрали? ")
        
    if number_save == "1":
        with open('phone_book.csv', 'w', encoding='utf-8') as file_csv:
            for key in phone_book_dict.keys():
                file_csv.write(f"{key} : {phone_book_dict[key]}")

    if number_save == "2":
        with open('phone_book.json', 'w') as file_json:
            for key in phone_book_dict.keys():
                file_json.write(f"{key} : {phone_book_dict[key]}")
        
    if number_save == "3":
        with open('phone_book.txt', 'w', encoding='utf-8') as file_txt:
            for key in phone_book_dict.keys():
                file_txt.write(f"{key} : {phone_book_dict[key]}")
        

def view_all_contacts():
    print(phone_book_dict)

def find_a_contact():
    last_name = input("Введите фамилию: ")
    name = input("Введите имя: ")
    middle_name = input("Введите оnчество: ")
    print(f"{last_name, name, middle_name} : {phone_book_dict[last_name, name, middle_name]}")

def add_contact():
    last_name = input("Введите фамилию: ")
    name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    mobile_phone = input("Введите номер мобильного телефона: ")
    email = input("Введите электронную почту: ")
    phone_book_dict[last_name, name, middle_name] = mobile_phone, email
    
def load_phone_book():

    print("Выберите формат для загрузки фаила")
    print("    1 - csv")
    print("    2 - json")
    print("    3 - txt")

    number_load = input("Что Вы выбрали? ")        
    
    if number_load == "3":
        
        with open("phone_book.txt", "r", encoding="utf-8") as file_txt:
            for key in file_txt.keys():
                file_txt.write(f"{key} : {phone_book_dict[key]}")

    if number_load == "2":
        with open('phone_book.json', 'r') as file_json:
            phone_book_dict = json.load(file_json)

    if number_load == "1":
        with open('phone_book.csv', 'r') as file_csv:
            csv.reader(file_csv)

def delete_contact():
    last_name = input("Введите фамилию: ")
    name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    del phone_book_dict[last_name, name, middle_name]

def delete_all_contacts():
    phone_book_dict.clear()

def main():
    menu()

phone_book_dict = {}    

if __name__ == '__main__':
    main()