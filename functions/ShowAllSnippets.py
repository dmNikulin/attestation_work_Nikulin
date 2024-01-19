def data_read():
    with open('attestation_work_Nikulin\snippets_data\snippets.csv', 'r', encoding = 'utf-8') as data:
        return data.read()

def read_snippets():
    data = data_read()
    print(data)