import os
from service.NoteDataService import NoteDataService
from view.NotesAppView import NotesAppView
from model.ConsoleMenu import ConsoleMenu
from service.TitleSpecification import TitleSpecification
from service.TitleFilter import TitleFilter
from service.ContentSpecification import ContentSpecification
from service.ContentFilter import ContentFilter


class NoteController:
    note_service = NoteDataService()
    view = NotesAppView()

    def __init__(self):
        self.view.set_function_new_note(self.__func_create_note)
        self.view.set_function_edit_note(self.__func_edit_note)
        self.view.set_function_delete_note(self.__func_delete_note)
        self.view.set_function_search_by_title(self.__filter_by_title)
        self.view.set_function_search_by_content(self.__filter_by_content)
        self.view.set_list_notes_menu(self.note_service.get_notes())

    def start(self):
        self.view.show_main_menu()

    def __func_create_note(self):
        try:
            ConsoleMenu.draw_title('---NEW NOTE---')
            title = self._input_title()
            content = self._input_content()
            if title is not None and content is not None:
                self.note_service.create(title=title, content=content)
                print('The record has been saved successfully!')
            else:
                pass  # log
            user_choice = input('Would you like to continue? Y/N: ')
            if user_choice.lower() == 'y':
                self.view.set_list_notes_menu(self.note_service.get_notes())
                os.system('cls||clear')
                self.view.show_main_menu()
            else:
                print('The program is completed.')
        except Exception as e:
            print(e)

    def __func_edit_note(self, id_note):
        try:
            ConsoleMenu.draw_title('---EDITE NOTE---')
            title = self._input_title()
            content = self._input_content()
            self.note_service.update(id=id_note, title=title, content=content)
            print('The record has been saved successfully!')
            user_choice = input('Would you like to continue? Y/N: ')
            if user_choice.lower() == 'y':
                self.view.set_list_notes_menu(self.note_service.get_notes())
                os.system('cls||clear')
                self.view.show_main_menu()
            else:
                print('The program is completed.')
        except Exception as e:
            print(e)

    def __func_delete_note(self, id_note):
        try:
            user_choice = input('Are you sure you want to delete the record? Y/N: ')
            if user_choice.lower() == 'y':
                self.note_service.delete(id=id_note)
                print('The note has been deleted.')
            else:
                print('The operation was canceled.')
            self.view.set_list_notes_menu(self.note_service.get_notes())
            os.system('cls||clear')
            self.view.show_list_notes_menu()
        except Exception as e:
            print(e)

    def __filter_by_title(self):
        filter_value = self._input_filter_value()
        spec_title = TitleSpecification(filter_value)
        filter_notes = TitleFilter.filter(self.note_service.get_notes(), spec_title)
        self.view.set_filter_notes_menu(filter_notes)
        self.view.show_filter_notes_menu()

    def __filter_by_content(self):
        filter_value = self._input_filter_value()
        spec_title = ContentSpecification(filter_value)
        filter_notes = ContentFilter.filter(self.note_service.get_notes(), spec_title)
        self.view.set_filter_notes_menu(filter_notes)
        self.view.show_filter_notes_menu()

    def _input_title(self):
        try:
            title = input('Note title: ')
            if title == '':
                raise ValueError('The title of the note cannot be empty! Please, try again.')
            elif len(title) > 100:
                raise ValueError('The title of the note is too long! Please, try again.')
            return title
        except ValueError as e:
            print(e)
            self._input_title()

    def _input_content(self):
        try:
            content = input('Content: ')
            if content == '':
                raise ValueError('The context of the note cannot be empty! Please, try again.')
            return content
        except ValueError as e:
            print(e)
            self._input_content()

    def _input_filter_value(self):
        title = input('Filter value: ')
        return title
