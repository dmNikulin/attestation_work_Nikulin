import datetime

def snippet_content():
    text = input('Заметка: ')
    final_text = ''
    counter = 10                                #Количество слов в одной строчке

    for i in text.split(' '):
        if counter != 0:
            final_text = final_text + i + ' '
            counter = counter - 1

        if counter == 0:
            final_text = final_text + '  ' + '\n'
            counter = 10

    current_date = str(datetime.date.today())
    print()
    return (final_text + '\n' + current_date)

def add_snippet(title):
    with open(f'attestation_work_Nikulin\snippets_data\{title}.csv', 'a', encoding = 'utf-8') as data:
        data.write(snippet_content())
        print('\n Заметка успешно сохранена!')
        print()