from functions import CreateNewSnippet

cmd = 0

def user_interface():
    while cmd != '4':
        print('Меню:\n'
            '1. Новая заметка\n'
            '2. Вывести заметки\n'
            '3. Редактировать заметку\n'
            '4. Удалить заметку\n'
            '5. Выход\n')
        cmd = int(input('Введите номер операции: '))
        print()

        while cmd not in ('1', '2', '3', '4', '5'):
            print('Некорректный ввод')
            cmd = int(input('Введите номер операции: '))

            match cmd:
                case '1':
                    add_snippet()

                case '2':
                    print_contacts()

                case '3':
                    search_contacts()
                
                case '4':
                    print('До свидания!')