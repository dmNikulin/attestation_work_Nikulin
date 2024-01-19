from functions.CreateNewSnippet import *
from functions.ShowAllSnippets import *


def user_interface():
    cmd = None

    while cmd != '5':
        print('Меню:\n'
              '1. Новая заметка\n'
              '2. Вывести заметки\n'
              '3. Редактировать заметку\n'
              '4. Удалить заметку\n'
              '5. Выход\n')
        cmd = input('Введите номер операции: ')
        print()

        if cmd not in ('1', '2', '3', '4', '5'):
            print('Некорректный ввод')
            cmd = input('Введите номер операции: ')

        match cmd:
            case '1':
                snippet_title = input('Введите название заметки: ')
                add_snippet(snippet_title)

            case '2':
                read_snippets()

            case '3':
                read_snippets()

            #     case '4':
            #         print('До свидания!')
