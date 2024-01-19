def snippet_content():
    title = input('Введите название заметки: ')
    text = input('Заметка: ')
    return (title + '\n' + text)

def add_snippet():
    with open('attestation_work_Nikulin\snippets_data\snippets.csv', 'a', encoding = 'utf-8') as data:
        data.write(snippet_content())
        print('\n Заметка успешно сохранена!')
        print()