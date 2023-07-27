from Notes_app.model.Note import Note
from Notes_app.service.NoteService import NoteService

notes_service = NoteService()
notes_service.create(title="test", content="Today was a typical school day for me", priority=Note.Priority.lower)
notes_service.create(title="test", content="Today was a typical school day for me", priority=Note.Priority.medium)
notes_service.create(title="test Hello", content="Hobby is an activity that we do for fun, just because we like it.")
notes_service.create(title="I love Python", content="Drawing comics is not the same as just drawing.",
                     priority=Note.Priority.high)
notes_service.update(id=2, title="test or no", content="Most people would agree that it is great to have a pet.")
notes_service.delete(id=3)

notes = notes_service.get_notes()
for note in notes:
    print(str(note) + '\n')
