import os
import logging
from datetime import datetime
from service.NoteDataService import NoteDataService
from view.NotesAppView import NotesAppView
from model.ConsoleMenu import ConsoleMenu
from service.NoteSpecification import NoteSpecification
from service.TitleFilter import TitleFilter
from service.ContentFilter import ContentFilter

from service.DateFilter import DateFilter


class NoteController:
    note_service = NoteDataService()
    view = NotesAppView()
    logging.basicConfig(level=logging.ERROR,
                        filename="notes_app_log.log",
                        format="%(asctime)s | %(levelname)s | %(message)s")

    def __init__(self):
        try:
            self.view.set_function_new_note(self.__func_create_note)
            self.view.set_function_edit_note(self.__func_edit_note)
            self.view.set_function_delete_note(self.__func_delete_note)
            self.view.set_function_search_by_title(self.__filter_by_title)
            self.view.set_function_search_by_content(self.__filter_by_content)
            self.view.set_function_search_by_date(self.__filter_by_date)
            self.view.set_list_notes_menu(self.note_service.get_notes())
        except Exception:
            logging.error("Init NoteController:", exc_info=True)

    def start(self):
        """
        Method for displaying the main menu in the console.
        """
        try:
            self.view.show_main_menu()
        except Exception:
            logging.error("Start program:", exc_info=True)

    def __func_create_note(self):
        """
        The function is intended for an item from the main menu to create a new note.
        """
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
        except Exception:
            logging.error("Start method to create note:", exc_info=True)

    def __func_edit_note(self, id_note):
        """
        The function is intended for an item from the note detail menu to edit a note.
        """
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
        except Exception:
            logging.error("Start method to edit note:", exc_info=True)

    def __func_delete_note(self, id_note):
        """
        The function is intended for an item from the note detail menu to edit a note.
        """
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
        except Exception:
            logging.error("Start method to delete note:", exc_info=True)

    def __filter_by_title(self):
        """
        The function is intended for an item from the search menu, for filtering notes by title.
        """
        try:
            filter_value = self._input_filter_value('Enter title: ')
            spec_title = NoteSpecification(filter_value)
            filter_notes = TitleFilter.filter(self.note_service.get_notes(), spec_title)
            self.view.set_filter_notes_menu(filter_notes)
            self.view.show_filter_notes_menu()
        except Exception:
            logging.error("Start method to filter by title:", exc_info=True)

    def __filter_by_content(self):
        """
        The function is intended for an item from the search menu, for filtering notes by content.
        """
        try:
            filter_value = self._input_filter_value('Enter content: ')
            spec_title = NoteSpecification(filter_value)
            filter_notes = ContentFilter.filter(self.note_service.get_notes(), spec_title)
            self.view.set_filter_notes_menu(filter_notes)
            self.view.show_filter_notes_menu()
        except Exception:
            logging.error("Start method to filter by content:", exc_info=True)

    def __filter_by_date(self):
        """
        The function is intended for an item from the search menu, for filtering notes by date.
        """
        try:
            filter_value = self._input_filter_value('Enter date (YYYY-MM-DD): ')
            while not self._check_date(filter_value):
                filter_value = self._input_filter_value('Enter date (YYYY-MM-DD): ')
            spec_title = NoteSpecification(filter_value)
            filter_notes = DateFilter.filter(self.note_service.get_notes(), spec_title)
            self.view.set_filter_notes_menu(filter_notes)
            self.view.show_filter_notes_menu()
        except Exception:
            logging.error("Start method to filter by date:", exc_info=True)

    def _input_title(self):
        try:
            title = input('Note title: ')
            if title == '':
                raise ValueError('The title of the note cannot be empty! Please, try again.')
            elif len(title) > 50:
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

    def _input_filter_value(self, message):
        value = input(f'{message}: ')
        return value

    def _check_date(self, date):
        try:
            format_date = "%Y-%m-%d"
            datetime.strptime(date, format_date)
            return True
        except ValueError:
            print('Incorrect data format. Please try again.')
            return False
