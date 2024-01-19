import datetime

def snippet_content():
    text = input('Заметка: ')
    current_date = str(datetime.date.today())
    print()
    return (text + '\n' + current_date)

def add_snippet(title):
    with open(f'attestation_work_Nikulin\snippets_data\{title}.csv', 'a', encoding = 'utf-8') as data:
        data.write(snippet_content())
        print('\n Заметка успешно сохранена!')
        print()