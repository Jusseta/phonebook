import json


PHONEBOOK_FILE = 'phonebook.json'


def load_phonebook():
    """Загрузка данных из справочника"""
    try:
        with open(PHONEBOOK_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_phonebook(phonebook):
    """Сохранение данных в справочник"""
    with open(PHONEBOOK_FILE, 'w') as file:
        json.dump(phonebook, file)


def display_contacts(contacts, page):
    """Вывод списка контактов постранично"""
    page_size = 10
    if contacts:
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        for index, contact in enumerate(contacts[start_index:end_index], start=start_index + 1):
            print(f'{index}. {contact}')
    else:
        print('В справочнике пока нет контактов')


def add_contact(phonebook):
    """Добавление нового контакта в справочник"""
    contact = {}
    contact['last_name'] = input('Ваша фамилия: ')
    contact['first_name'] = input('Ваше имя: ')
    contact['patronymic'] = input('Ваше отчество: ')
    contact['organization'] = input('Название организации: ')
    contact['work_phone'] = input('Ваш рабочий телефон: ')
    contact['private_phone'] = input('Ваш личный телефон: ')
    phonebook.append(contact)
    save_phonebook(phonebook)
    print('Контакт успешно добавлен')


def edit_contact(phonebook):
    """Изменение контакта в справочнике"""
    last_name = input('Введите фамилию контакта для редактирования: ')
    for contact in phonebook:
        if contact['last_name'] == last_name:
            contact['first_name'] = input('Новое имя: ')
            contact['patronymic'] = input('Новое отчество: ')
            contact['organization'] = input('Новая организация: ')
            contact['work_phone'] = input('Новый рабочий телефон: ')
            contact['private_phone'] = input('Новый личный телефон: ')
            save_phonebook(phonebook)
            print('Контакт обновлен')
            return
        else:
            print('Контакт не найден')
            break


def search_contacts(phonebook):
    """Поиск по контактам"""
    search = input('Поиск: ').lower()
    found_contacts = []
    for contact in phonebook:
        if (search in contact['last_name'].lower() or
            search in contact['first_name'].lower() or
            search in contact['patronymic'].lower() or
            search in contact['organization'].lower() or
            search in contact['work_phone'] or
            search in contact['private_phone']):
            found_contacts.append(contact)
    if found_contacts:
        print(f'Найденные контакты:\n {found_contacts}')
    else:
        print('Контакты не найдены')


def main():
    phonebook = load_phonebook()

    while True:
        print('\nМеню:\n'
              '1. Вывести контакты\n'
              '2. Добавить контакт\n'
              '3. Редактировать контакт\n'
              '4. Поиск контактов\n'
              '5. Выйти')

        choice = input('Выберите действие: ')
        if choice == '1':
            page = int(input("Введите номер страницы: "))
            display_contacts(phonebook, page)
        elif choice == '2':
            add_contact(phonebook)
        elif choice == '3':
            edit_contact(phonebook)
        elif choice == '4':
            search_contacts(phonebook)
        elif choice == '5':
            print('Выход из программы')
            break
        else:
            print('Неверное действие. Попробуйте ещё раз')


if __name__ == "__main__":
    main()
