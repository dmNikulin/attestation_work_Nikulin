def read_snippets():
    with open('snipets.csv', 'r', encoding = 'utf-8') as data:
        return data.read()