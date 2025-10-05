from notebook import Notebook
from clean import clean

notebook = Notebook()


def menu():
    print('1. Create note\n2. List of notes\n3. Read note\n4. Edit note\n5. Delete note\n6. Exit')


while True:
    clean()
    menu()
    choice = input('> ')

    match choice:
        case '1':
            clean()
            notebook.create_note()

        case '2':
            clean()
            notebook.list_notes()
            print()
            input('Press Enter to continue')

        case '3':
            clean()
            notebook.list_notes()
            index = ''
            while not isinstance(index, int):
                try:
                    index = int(input('Enter the index of the note (to exit without deleting enter any number outside '
                                      'the list or if list is empty):\n> '))
                except ValueError:
                    pass
            clean()
            notebook.read_note(index)
            print()
            input('Press Enter to continue')

        case '4':
            clean()
            notebook.list_notes()
            index = ''
            while not isinstance(index, int):
                try:
                    index = int(input('Enter the index of the note (to exit without deleting enter any number outside '
                                      'the list or if list is empty):\n> '))
                except ValueError:
                    pass
            notebook.edit_note(index)

        case '5':
            clean()
            notebook.list_notes()
            print()
            index = ''
            while not isinstance(index, int):
                try:
                    index = int(input('Enter the index of the note (to exit without deleting enter any number outside '
                                      'the list or if list is empty):\n> '))
                    print(type(None))
                    print(index)
                except ValueError:
                    pass
            notebook.delete_note(index)

        case '6':
            exit()

        case _:
            print('Your choice doesn\'t fit any options')
            print()
            input('Press Enter to continue')
