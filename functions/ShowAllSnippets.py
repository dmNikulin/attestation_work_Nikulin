import os


def show_all_snippets():
    # Указываем путь к директории
    directory = "attestation_work_Nikulin/snippets_data/"

    # Получаем список файлов
    files = os.listdir(directory)

    number_of_snippet = 0

    for i in files:
        number_of_snippet += 1
        print(f'{number_of_snippet}) {i}')

    print()