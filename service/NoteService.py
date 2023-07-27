from Notes_app.model.Note import Note
from Notes_app.service.DataService import DataService


class NoteService(DataService):

    def __init__(self):
        self._notes = list()

    def get_notes(self):
        return self._notes

    def create(self, **kwargs):
        id_note = self.__get_id()
        title = kwargs.get('title')
        content = kwargs.get('content')
        priority = kwargs.get('priority')
        new_note = Note(id_note, title, content)
        if priority is not None:
            new_note.set_priority(priority)
        self._notes.append(new_note)

    def update(self, **kwargs):
        id_update_note = kwargs.get('id')
        title = kwargs.get('title')
        content = kwargs.get('content')
        priority = kwargs.get('priority')
        if id_update_note is not None:
            for note in self._notes:
                if note.get_id() == id_update_note:
                    note.set_title(title) \
                        .set_content(content)
                    if priority:
                        note.set_priority(priority)
                    return

    def delete(self, **kwargs):
        id_delete_note = kwargs.get('id')
        if id_delete_note is not None:
            del_index = self.__get_index_by_id(id_delete_note)
            self._notes.pop(del_index)

    def __get_id(self):
        last_id = 1
        for _ in self._notes:
            last_id += 1
        return last_id

    def __get_index_by_id(self, value):
        for index, note in enumerate(self._notes):
            if note.get_id() == value:
                return index
