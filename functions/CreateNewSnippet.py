def snippet_content():
    title = input('Введите название заметки: ')
    text = input('Заметка: ')
    return (title + '\n' + text)

def add_snippet():
    with open('./snipets_data/snipets.csv', 'a', encoding = 'utf-8') as data:
        data.write(snippet_content())