from functions.ShowAllSnippets import *


def edit_snippets():
    directory = "attestation_work_Nikulin/snippets_data/"

    files = os.listdir(directory)

    cmd = None

    while cmd != 0:
        show_all_snippets()

        print('Введите номер заметки для редактирования или "0" для выхода:')
        cmd = int(input())

        for i in range(len(files)):
            if i == cmd-1:
                f = open(f'attestation_work_Nikulin\snippets_data\{files[i]}', 'r')
                lines = f.readlines()
                d = open(f'attestation_work_Nikulin\snippets_data\{files[i]}', 'r')
                print(d.read() + '\n')
                which_line = (int(input("Какую строку хотите заменить: "))) - 1
                lines[which_line] = input("Введите изменения:") + '\n'
                print()
                f.close()
                d.close()

                with open(f'attestation_work_Nikulin\snippets_data\{files[i]}', 'w') as data:
                    data.writelines(lines)
                    print("Изменения успешно внесены!")
                    print()
