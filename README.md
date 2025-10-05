# Console Notes Manager

Python notes manager made in console.

## Features

- **Creating notes**: allows to create new notes
- **Listing notes**: shows the list of all notes in the folder
- **Reading notes**: allows to read created notes
- **Editing notes**: allows to edit notes
- **Deleting notes**: allows to delete unwanted notes

## Installation

```bash
git clone https://github.com/n1n4zu/Console_notes_manager.git
cd Console_notes_manager
```

## Usage

### Windows
```bash
python main.py
```

### Linux
```bash
python3 main.py
```

## Class documentation

### `Notebook` Class

#### Methods

| **Method**                                | **Description**                                                                                               |
|-------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| **`create_note(self) -> None`**           | Creates a new note by taking user input for title and content, then saves it as JSON in the `notes` folder    |
| **`list_notes() -> None`**                | Static method that shows the list of the notes in `notes` folder                                              |
| **`read_note(index: int) -> None`**       | Static method that shows title, create date, last modification date and text of the note with given index     |
| **`edit_note(self, index: int) -> None`** | Allows editing title or content of a note by index. When title changes, creates new file and removes old one  |
| **`delete_note(index: int) -> None`**     | Static method that deletes the note with given index                                                          |

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## File Structure

Console_notes_manager/ \
├── notes/ # Directory where notes are stored as JSON files \
├── main.py # Main application entry point \
├── notebook.py # Notebook class implementation \
├── clean.py # Console clearing utility \
└── [README.md](README.md) # This file

## License

MIT License - See [LICENSE](LICENSE) for details