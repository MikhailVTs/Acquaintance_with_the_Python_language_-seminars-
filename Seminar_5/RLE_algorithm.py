def creating_a_text_document():
    with open('creat_text.txt', 'w') as data:
        data.write('WWWWWWWWWBBBWWWWWWWWWWABCABCABCDDDFFFFFFWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')

def reading_a_text_document():
    with open('creat_text.txt', 'r') as data:
        read_file = data.read()
    print(read_file)

def text_document_entry(s): 

    algorithm_RLE = '' 

    with open('creat_text.txt', 'r') as data:
        read_file = data.read()    

    i = 0
    while i < len(read_file):

        count = 1
    
        while i + 1 < len(read_file) and read_file[i] == read_file[i + 1]:
            count = count + 1
            i = i + 1
        algorithm_RLE += str(count) + read_file[i]
        i = i + 1
    
    with open('entry_text.txt', 'w') as data:
        data.write(algorithm_RLE)
    
    return algorithm_RLE  

def main():
    creating_a_text_document()
    reading_a_text_document()
    print(text_document_entry(reading_a_text_document()))

if __name__ == '__main__':
    main()