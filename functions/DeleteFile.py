import os
from functions.ShowAllSnippets import *

def deleteFile():

    directory = "attestation_work_Nikulin/snippets_data/"

    files = os.listdir(directory)

    cmd = None

    while cmd != 0:
        show_all_snippets()

        print('Введите номер заметки для удаления или "0" для выхода:')
        cmd = int(input())

        for i in range(len(files)):
            if i == cmd-1:
                os.remove(f'attestation_work_Nikulin/snippets_data/{files[i]}')
                print('Заметка удалена.' + '\n')
                cmd = 0
                break
            if cmd > len(files):
                print("Такой заметки не существует!")
