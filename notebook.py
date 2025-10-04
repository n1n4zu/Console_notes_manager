import json
from datetime import datetime, timezone
from os import scandir, remove
from clean import clean


class Notebook:
    """
    Console Notes Manager

    A comprehensive note management system that stores notes as JSON files
    in a dedicated 'notes' folder. Supports full CRUD operations (Create,
    Read, Update, Delete) with a console-based interface.

    Notes are automatically sorted alphabetically by filename and include
    metadata like creation and modification dates.

    Attributes:
        Does not maintain public attributes. Uses private attributes for
        internal state management.
    """

    def __init__(self) -> None:
        self.__choice = None
        self.__current_time = datetime.now(timezone.utc).isoformat()

    def create_note(self) -> None:
        """
        Creates a new note by taking user input for title and content, then saves it as JSON in the `notes` folder
        """
        title = input('Name your note:\n> ').replace(' ', '_')

        lines = []
        print()
        line = input('Enter your note (to finish press Ctrl+D (Linux/Mac) lub Ctrl+Z + Enter '
                     '(Windows)):\n> ')
        lines.append(line)
        try:
            while True:
                line = input()
                lines.append(line)
        except EOFError:
            # Ctrl+D (Linux/Mac) lub Ctrl+Z + Enter (Windows)
            pass
        note = '\n'.join(lines)

        data = {
            'title': title,
            'create_date': self.__current_time,
            'last_mod': self.__current_time,
            'note': note
        }

        with open(f'notes/{title}.json', 'w', encoding='utf-8') as file:
            json.dump(data, file)

    @staticmethod
    def list_notes() -> None:
        """
        Static method that shows the list of the notes in `notes` folder
        """
        with scandir('notes') as entries:
            sorted_entries = sorted([entry for entry in entries if entry.is_file()], key=lambda e: e.name)

            for i, entry in enumerate(sorted_entries, 1):
                print(f'{i}. {entry.name}')

    @staticmethod
    def read_note(index: int) -> None:
        """
        Static method that shows title, create date, last modification date and text of the note with given index
        :param index: Index of the note
        """
        with scandir('notes') as entries:
            sorted_entries = sorted([entry for entry in entries if entry.is_file()], key=lambda e: e.name)

            if 0 <= index - 1 < len(sorted_entries):
                target_entry = sorted_entries[index - 1]
                try:
                    with open(target_entry.path, 'r', encoding='utf-8') as file:
                        data = json.load(file)
                        create_date = datetime.fromisoformat(data['create_date'])
                        last_mod = datetime.fromisoformat(data['last_mod'])
                        print(f'Title: {data['title']}')
                        print(f'Create date: {create_date.strftime('%Y-%m-%d %H:%M')}     '
                              f'Last modification: {last_mod.strftime('%Y-%m-%d %H:%M')}')
                        print()
                        print(data['note'])
                except json.JSONDecodeError:
                    print(f"Error parsing JSON in file {target_entry.name}")
            else:
                print(f"There is no note about the index {index}.")

    def edit_note(self, index: int) -> None:
        """
        Allows editing title or content of a note by index. When title changes, creates new file and removes old one
        :param index: Index of the note
        """
        with scandir('notes') as entries:
            sorted_entries = sorted([entry for entry in entries if entry.is_file()], key=lambda e: e.name)

            if 0 <= index - 1 < len(sorted_entries):
                target_entry = sorted_entries[index - 1]
                try:
                    with open(target_entry.path, 'r', encoding='utf-8') as file:
                        data = json.load(file)
                        create_date = datetime.fromisoformat(data['create_date'])
                        last_mod = datetime.fromisoformat(data['last_mod'])
                        print(f'Title: {data['title']}')
                        print(f'Create date: {create_date.strftime('%Y-%m-%d %H:%M')}     '
                              f'Last modification: {last_mod.strftime('%Y-%m-%d %H:%M')}')
                        print()
                        print(data['note'])
                        print()

                        self.__choice = input('What would you like to edit?\n1. Title\n2. Note\n3. Exit\n> ')
                        clean()

                        match self.__choice:
                            case '1':
                                data['title'] = input('New title:\n> ').replace(' ', '_')
                                while data['title'] == '':
                                    data['title'] = input('New title:\n> ').replace(' ', '_')
                                data['last_mod'] = self.__current_time
                                
                            case '2':
                                data['note'] = ''
                                data['last_mod'] = self.__current_time
                                lines = []
                                print()
                                line = input('Enter your note (to finish press Ctrl+D (Linux/Mac) lub Ctrl+Z + Enter '
                                             '(Windows)):\n> ')
                                lines.append(line)
                                try:
                                    while True:
                                        line = input()
                                        lines.append(line)
                                except EOFError:
                                    # Ctrl+D (Linux/Mac) lub Ctrl+Z + Enter (Windows)
                                    pass
                                data['note'] = '\n'.join(lines)

                            case '3':
                                return

                            case _:
                                print('Your choice doesn\'t fit any options')
                                return

                        with open(f'notes/{data['title']}.json', 'w', encoding='utf-8') as f:
                            json.dump(data, f)

                    if self.__choice == '1':
                        remove(target_entry.path)

                except json.JSONDecodeError:
                    print(f"Error parsing JSON in file {target_entry.name}")
            else:
                print(f"There is no note about the index {index}.")

    @staticmethod
    def delete_note(index: int) -> None:
        """
        Static method that deletes the note with given index
        :param index: Index of the note
        """
        with scandir('notes') as entries:
            sorted_entries = sorted([entry for entry in entries if entry.is_file()], key=lambda e: e.name)

            if 0 <= index - 1 < len(sorted_entries):
                target_entry = sorted_entries[index - 1]
                try:
                    remove(target_entry.path)
                except json.JSONDecodeError:
                    pass
            else:
                print(f"There is no note about the index {index}.")
