# на Отлично в одного человека надо сделать консольное приложение Телефонный 
# справочник с внешним хранилищем информации, и чтоб был реализован основной 
# функционал - +просмотр, +сохранение, ?импорт, +поиск, +удаление, +изменение данных.

# Телефонный справочник

import json
# Блок работы с файлами
# функция загрузки из файла информации
def read_file():
    with open('phonebook.json', 'r') as f:
        data = f.read()
        book = eval(data)
        return(book)

# функция переписывает содержимое файла
def write_file(dict):
    with open('phonebook.json', 'w') as f:
        f.write(json.dumps(dict))

# Блок работы со словарем
# Ищем существующий контакт
def find_contact():
    name = input('Введите имя контакта: ')
    data = read_file()
    if len(data) == 0:
        print("В телефонной книге нет контактов")
    else:
        if name in data:
            value = data[name]
            print(f'У абонента "{name}" номер телефона: {value}')
        else:
            print(f'Контакт "{name}" в телефонном справочнике отсутствует')

#Сохраняем новый контакт
def save_contact():
    data = read_file()
    name = input("Введите имя контакта: ")
    number = input("Введите номер телефона без пробелов: ")
    if examination_number(number):
        int_number = int(number)
        if name in data:
            print('Такой контакт уже есть!')
        else:
            data[name] = int_number
            print('Контакт добавлен!')
            write_file(data)
    else:
        print("Вы неверно ввели номер телефона! Контакт не сохранен!")




# Изменить контакт
def change_contact():
    data = read_file()
    name = input("Введите имя контакта, которое хотите изменить: ")
    if name in data:
        new_name = input("Введите новое имя контакта: ")
        new_number = input("Введите новый номер контакта: ")
        if examination_number(new_number):
            int_number = int(new_number)    
            del data[name]
            data[new_name] = int_number
            print('Контакт изменен!')
            write_file(data)
        else:
            print("Вы неверно ввели номер телефона! Контакт не изменен!") 
    else:
        print('Такого контакта нет, но вы можете его создать используя функцию "сохранить".')

# Удалить контакт    
def delete_contact():
    data = read_file()
    name = input("Введите имя контакта, которое хотите удалить: ")
    if name in data:
        del data[name]
        print('Контакт удалён!')
        write_file(data)

# Импорт контакта
def import_contact():
    new_file = input("Введите название файла в который необходимо импоритировать контакты: ")
    data = read_file()
    with open(new_file, 'w') as f:
        f.write(json.dumps(data))
    with open(new_file, 'r') as f:
        new_data = f.read()
        book = eval(new_data)
        print(book)


# Блок проверки введенного номера телефона
# Проверка можно ли преобразовать строку в число
def is_numeric(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
# Проверка правильно введенного номера
def examination_number(numb):
    if is_numeric(numb):
        int_numb = int(numb)
        if (int_numb >=99 and int_numb <= 100000000000000):
            return True
        else:
            return False
    else:
        return False


# Команды работы телефонной книги
print(read_file())
save_contact()
print(read_file())
change_contact()
print(read_file())
delete_contact()
print(read_file())
import_contact()


