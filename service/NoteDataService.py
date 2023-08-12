import time
from model.Note import Note
from service.DataService import DataService
from service.FileSevice import FileService
from datetime import date


class NoteDataService(DataService):
    _notes = dict()

    def __init__(self):
        data = FileService().read_file('data.json')
        if data is not None:
            for value in data.values():
                self.create(id=value.get('id'),
                            title=value.get('title'),
                            content=value.get('content'),
                            date_of_create=value.get('date_of_create'),
                            date_of_update=value.get('date_of_update'))

    def get_notes(self):
        return self._notes

    def create(self, **kwargs):
        """
        Creates an instance of the Note class. Updates and writes data to a file.

        :param kwargs: title, content (required parameters),
        id, date_of_create, date_of_update (additional parameters)
        """
        id_note = kwargs.get('id')
        if id_note is None:
            id_note = self.__get_id()
        title = kwargs.get('title')
        content = kwargs.get('content')
        date_of_create = kwargs.get('date_of_create')
        if date_of_create is None:
            date_of_create = str(date.today())
        date_of_update = kwargs.get('date_of_update')
        new_note = Note(id_note, title, content, date_of_create, date_of_update)
        self._notes[id_note] = new_note
        data_file = {key: value.get_data() for (key, value) in self._notes.items()}
        FileService().write_to_file(data_file, 'data.json')

    def update(self, **kwargs):
        """
        Updates an instance of the Note class. Updates and writes data to a file.

        :param kwargs: id, title, content (required parameters)
        """
        id_update_note = kwargs.get('id')
        title = kwargs.get('title')
        content = kwargs.get('content')
        if id_update_note is not None:
            note = self._notes.get(id_update_note)
            note.set_title(title). \
                set_content(content). \
                set_date_of_update()
        data_file = {key: value.get_data() for (key, value) in self._notes.items()}
        FileService().write_to_file(data_file, 'data.json')

    def delete(self, **kwargs):
        """
        Updates an instance of the Note class. Updates and writes data to a file.

        :param kwargs: id the Note class instance (required parameters)
        """
        id_delete_note = kwargs.get('id')
        if id_delete_note is not None and self._notes.get(id_delete_note) is not None:
            self._notes.pop(id_delete_note)
            data_file = {key: value.get_data() for (key, value) in self._notes.items()}
            FileService().write_to_file(data_file, 'data.json')

    def __get_id(self):
        return str(round(time.time()))
