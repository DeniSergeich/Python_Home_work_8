def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('book.txt', 'r', encoding='utf-8') as file:
        print(file.read())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО: ')
    phone = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{fio} | {phone}')


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    print(data + '\n')    
    data_to_find = input('Введите данные для поиска: ')
    result = search(data, data_to_find)    
    if len(result) == 0:        
        print('\nСовпадений не найдено\n')        
        return        
    else:
        print('\n')                   
        print(*result, sep = '\n')
        print('\n')    
    mode = input('Требуется уточнение поиска? \nЕсли требуется, введите Да. Если нет, нажмите Enter: ')
    mode = mode.lower()
    if mode == 'да':
        print(accuracy_search(result) + '\n')
    



def search(book: str, info: str) -> str:
    """Находит в списке записи по определенному критерию поиска"""
    book = book.split('\n')
    search_list = []    
    for contact in book:
        if info in contact:
            search_list.append(contact)                
    return search_list


def accuracy_search(search_list: str) -> str:
    """Производит поиск по уточнению"""
    accuracy_list = []
    mode = input('\nВведите уточнение поиска: ')
    print('\n')    
    for item in search_list:        
        if mode in item.split():
            accuracy_list.append(item)            
    if len(accuracy_list) == 1:
        return accuracy_list[0]
    else:
        print('Требуется уточнение: ')
        print(*accuracy_list, sep = '\n')
        return accuracy_search(accuracy_list)
