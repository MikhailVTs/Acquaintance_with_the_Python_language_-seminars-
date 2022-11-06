def reading_a_file(file_name): 
    with open(f'{file_name}.txt', 'r', encoding='utf-8') as file_txt: 
        data = [i.split('\n')[0] for i in file_txt.readlines()] 
        school_database[file_name] = [] 
        for i in data: 
            school_database[file_name].append(tuple(i.split(':'))) 

def search_and_print_childrens(lastname): 
    id = [i[0] for i in school_database[parents_childrens['parents']] if lastname in i][0]
    children = [i for i in school_database[parents_childrens['childrens']] if id == i[1]]
    print(*[' '.join(i[2:4]) + '\n' for i in children])

def main():
    reading_a_file(1) 
    reading_a_file(2) 
    search_and_print_childrens(name_parents)

school_database = {} 
parents_childrens = {'parents': 1, 'childrens': 2}

print()
name_parents = input("Введите фамилию Родителя, для поиска в базе школы учащихся детей: ")
print()

if __name__ == '__main__':
    main()