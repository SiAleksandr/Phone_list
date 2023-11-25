def main():
    file_name = 'phonebook.txt'
    flag = True
    while flag:
        print()
        print('1 - Показать весь справочник')
        print('2 - Простое добавление записи')
        print('3 - Внесение изменений')
        print('4 - Поиск по имени или фамилии')
        print('0 - Выход')
        answer = input('ВАШЕ ДЕЙСТВИЕ => ')
        if answer == '0':
            flag = False
        elif answer == '1':
            show_all(file_name = file_name)
        elif answer == '2':
            simple_add(file_name = file_name)
        elif answer == '3':
            redact_line(file_name = file_name)
        elif answer == '4':
            search_end(file_name = file_name)

def show_all(file_name: str):
    print()
    with open (file_name, 'r') as f:
        data = f.readlines()
        print(''.join(data))
    input('Нажмите Enter -> ')

def simple_add(file_name: str):
    new_string = create_string()
    print()
    print('Будет добавлена эта запись')
    print(f'{new_string}')
    print('Подтверждение -> Enter')
    ask = input('Для отмены любая буква и Enter -> ')
    if ask == '':
        with open(file_name, 'a', encoding = 'utf-8') as f:
            f.write(new_string + '\n')
    

def create_string():
    print('Можно к имени дописать отчество')
    print('через нижнее подчёркивание. Пример: Виктория_Викторовна')
    name_ = input('Введите имя или имя_отчество -> ')
    while ' ' in name_:
        name_ = input('Введите без пробелов -> ')
    surname = input('Введите фамилию -> ')
    while ' ' in surname:
        surname = input('Введите без пробелов -> ')
    phone = input('Введите номер телефона -> ')
    while ' ' in phone:
        phone = input('Введите без пробелов -> ')
    new_string = name_ + ' ' + surname + ' ' + phone
    return new_string

def get_list(file_name: str):
    content = list()
    f = open(file_name, 'r', encoding = 'utf-8')
    for line in f:
        content.append(line)
    f.close()
    # for i in range(len(content) - 1):
    #     content[i] = content[i].replace('\n', '')
    return content

def write_list(file_name: str, content):
    f = open(file_name, 'w', encoding = 'utf-8')
    for i in content:
        f.writelines(f'{i}')
    f.close()

def get_word(mess: str):
    word = input(mess)
    if ' ' in word:
        print('Если это имя и отчество, то их нужно написать')
        print('через символ нижнего подчёркивания, пример: Виктория_Викторовна')
        word = input('Введите правильно -> ')
        while ' ' in word:
            word = input('Введите без пробелов -> ')
    return word

def search(content):
    print()
    marker = 1
    redact = -1
    redact = int(redact)
    while marker != 0:
        if marker == 1:
            print('ПОИСК (Выход -> клавиша Enter без ничего)')
            word2 = 'zzz'
            word3 = 'zzz'
            word4 = 'zzz'
            word1 = get_word('Введите имя -> ')
            for i in range(len(content)):
                if word1 != '':
                    if word1 in content[i]:
                        print(content[i])
        if marker == 2:
            print('Выход -> клавиша Enter без ничего')
            word2 = get_word('Введите фамилию -> ')
            for i in range(len(content)):
                if word2 != '':
                    if word1 in content[i] and word2 in content[i]:
                        print(content[i])
        if marker == 3:
            print('Выход -> клавиша Enter без ничего')
            word3 = get_word('Введите отчество (если нет, повторите имя) -> ')
            for i in range(len(content)):
                if word3 != '':
                    if word1 in content[i] and word2 in content[i] and word3 in content[i]:
                        print(content[i])
        if marker == 4:
            print('Выход -> клавиша Enter без ничего')
            word4 = get_word('Введите номер телефона -> ')
            for i in range(len(content)):
                if word4 != '':
                    if word1 in content[i] and word2 in content[i] and word3 in content[i] and word4 in content[i]:
                        print(content[i])
                        redact = i
        marker += 1
        if word1 == '' or word2 == '' or word3 == '' or word4 == '':
            marker = 0
        if marker == 5:
            marker = 0
    return redact
def search_end(file_name: str):
    content = get_list(file_name)
    search(content)
        
def redact_line(file_name: str):
    content = get_list(file_name)
    print('\nНайдите и пропишите все части\nизменяемой записи')
    redact = search(content)
    redact = int(redact)
    if redact != -1:   
        print('Будет изменена эта запись:')
        print(f'{content[redact]}')
        print('Подтверждение -> Entre')
        ask = input('Для отмены любая буква и Enter -> ')
        if ask == '':
            print()    
            new = create_string()
            new += '\n'
            content[redact] = new
            write_list(file_name, content)
            print(f'{new} -> Эта запись успешно создана.')
            input('Нажмите Enter -> ')

if __name__ == '__main__':
    main()