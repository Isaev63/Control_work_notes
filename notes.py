import json
from datetime import datetime
import re


class Notes:
    """
    Class for working with notes.
    """

    def __init__(self, filename):
        """
        Creates an instance of the Notes class.
        Parameters:
            filename (str): The name of the file to store notes (without extension).
        Raises:
            ValueError: If the filename contains invalid characters.
        """
        if not re.match("^[a-zA-Z0-9_-а-яА-Я]+$", filename):
            raise ValueError("\033[1;31mИмя файла содержит недопустимые символы!\033[0m")
        self.filename = filename

    def create_note(self, title=None, text=None):
        """
        Creates a new note and saves it to the file.
        Data input is done through user input from the keyboard.
        """
        notes = self._load_notes()
        new_note = {
            'id': self._generate_id(notes),
            'date': datetime.now().strftime('%d-%m-%Y | %H:%M:%S'),
            'title': title or input('Введите заголовок: '),
            'text': text or input('Введите текст: ')
        }
        notes.append(new_note)
        self._save_notes(notes)
        self._sort_notes_date()
        print('\033[1;32m[*] -- Запись создана.\033[0m')
        return new_note

    def read_note(self, id_note):
        """
        Displays information about the note with the specified ID.
        Parameters:
            id_note (int): The ID of the note.
        """
        notes = self._load_notes()
        for note in notes:
            if note['id'] == id_note:
                print(self._note_to_str(note))
                return note
        return None

    def read_all_notes(self):
        """
        Displays a list of all notes.
        """
        notes = self._load_notes()
        for note in notes:
            print(f'{note["id"]}. {note["title"]} -- [{note["date"]}]')

    def edit_note(self, id_note, new_title=None, new_text=None):
        """
        Edits the note with the specified ID.
        Parameters:
            id_note (int): The ID of the note to be edited.
        """
        notes = self._load_notes()
        for note in notes:
            if note["id"] == id_note:
                note['date'] = datetime.now().strftime('%d-%m-%Y | %H:%M:%S')
                note['title'] = new_title or input('Введите заголовок: ')
                note['text'] = new_text or input('Введите текст: ')
                self._save_notes(notes)
                self._sort_notes_date()
                print('\033[1;32m[*] -- Запись отредоктированна.\033[0m')
                return note
        return None

    def delete_note(self, id_note):
        """
        Deletes the note with the specified ID.
        Parameters:
            id_note (int): The ID of the note to be deleted.
        """
        notes = self._load_notes()
        for note in notes:
            if note['id'] == id_note:
                notes.remove(note)
                self._save_notes(notes)
                self._sort_notes_date()
                print(f'\033[1;32m[*] -- Запись с ID "{id_note}" удалена.\033[0m')
                return True
        print(f'\033[1;31m[*] -- Запись с ID "{id_note}" не существует!\033[0m')
        return False

    def _load_notes(self):
        """
        Loads notes from the file.
        Returns:
            list: List of notes.
        """
        try:
            with open(f'{self.filename}.json', 'r', encoding='utf-8') as file:
                notes = json.load(file)
        except FileNotFoundError:
            notes = []
        return notes

    def _save_notes(self, notes):
        """
        Saves notes to the file.
        Parameters:
            notes (list): List of notes to be saved.
        """
        try:
            with open(f'{self.filename}.json', 'w', encoding='utf-8') as file:
                json.dump(notes, file, indent=4)
        except IOError:
            print('\033[1;31m[*] -- Ошибка при сохранении файла!\033[0m')

    def _sort_notes_date(self):
        """
        Sorts notes by their Date.
        """
        notes = self._load_notes()
        sorted_notes = sorted(notes, key=lambda x: datetime.strptime(x['date'], '%d-%m-%Y | %H:%M:%S'))
        self._save_notes(sorted_notes)

    def _generate_id(self, notes):
        """
        Generates a unique ID for a new note.
        Parameters:
            notes (list): List of existing notes.
        Returns:
            int: New ID for the note.
        """
        return max([note['id'] for note in notes], default=0) + 1

    def _note_to_str(self, note):
        """
        Formats a note as a string for displaying.
        Parameters:
            note (dict): The note to format.
        Returns:
            str: Formatted note as a string.
        """
        return f'ID: {note["id"]}\nDate: {note["date"]}\nTitle: {note["title"]}\nText: {note["text"]}'
