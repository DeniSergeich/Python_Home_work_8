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
    print(data)
    data_to_find = input('Введите данные для поиска: ')
    print(search(data, data_to_find))


def search(book: str, info: str) -> str:
    """Находит в списке записи по определенному критерию поиска"""
    book = book.split('\n')
    for contact in book:
        if info in contact:
            return contact
    return 'Совпадений не найдено'