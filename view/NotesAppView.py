import os
from model.ConsoleMenu import ConsoleMenu
from model.ItemMenu import ItemMenu


class NotesAppView:
    main_menu = ConsoleMenu('---NOTES APP---')
    list_notes_menu = ConsoleMenu('---LIST NOTES---')
    note_menu = ConsoleMenu('---NOTE MENU---')
    search_menu = ConsoleMenu('---SEARCH---')
    filter_notes_menu = ConsoleMenu('---REQUEST RESULT---')

    def __init__(self):
        self.main_menu.extend_items([ItemMenu('New note'),
                                     ItemMenu('Notes list', function=self.show_list_notes_menu),
                                     ItemMenu('Search', function=self.show_search_menu),
                                     ItemMenu('Exit', function=self.__exit)])
        self.note_menu.extend_items([ItemMenu('Edit'),
                                     ItemMenu('Delete'),
                                     ItemMenu('Exit', function=self.__exit)])
        self.search_menu.extend_items([ItemMenu('By title'),
                                       ItemMenu('By content'),
                                       ItemMenu('Exit', function=self.__exit)])

    def set_list_notes_menu(self, notes_list: dict):
        self.list_notes_menu.clear_items()
        if len(notes_list) != 0:
            for note in notes_list.values():
                self.list_notes_menu.add_item(
                    ItemMenu(note.get_title(), function=self.__note_detail, data=note.get_data()))
        self.list_notes_menu.add_item(ItemMenu('Exit', function=self.__exit))

    def set_filter_notes_menu(self, notes_list: dict):
        self.filter_notes_menu.clear_items()
        if len(notes_list) != 0:
            for note in notes_list.values():
                self.filter_notes_menu.add_item(
                    ItemMenu(note.get_title(), function=self.__note_detail, data=note.get_data()))
        self.filter_notes_menu.add_item(ItemMenu('Exit', function=self.__exit))

    def set_function_new_note(self, function):
        self.main_menu.get_item(0).set_function(function)

    def set_function_edit_note(self, function):
        self.note_menu.get_item(0).set_function(function)

    def set_function_delete_note(self, function):
        self.note_menu.get_item(1).set_function(function)

    def set_function_search_by_title(self, function):
        self.search_menu.get_item(0).set_function(function)

    def set_function_search_by_content(self, function):
        self.search_menu.get_item(1).set_function(function)

    def show_main_menu(self):
        self.main_menu.draw()
        values = [i + 1 for i in range(self.main_menu.len_items())]
        enter = self.__get_user_choice(values)
        action = self.main_menu.get_item(enter - 1).get_function()
        if action == -1:
            print('The program is completed.')

    def show_list_notes_menu(self):
        self.list_notes_menu.draw()
        values = [i + 1 for i in range(self.list_notes_menu.len_items())]
        enter = self.__get_user_choice(values)
        data = self.list_notes_menu.get_item(enter - 1).get_data()
        action = self.list_notes_menu.get_item(enter - 1).get_function_with_data(data)
        if action == -1:
            self.show_main_menu()

    def __note_detail(self, note):
        id_note = note.get('id')
        title = note.get('title')
        content = note.get('content')
        ConsoleMenu.draw_title(title)
        print(f'{content}')
        self.show_note_menu(id_note)

    def show_note_menu(self, id_note):
        self.note_menu.draw()
        values = [i + 1 for i in range(self.note_menu.len_items())]
        enter = self.__get_user_choice(values)
        action = self.note_menu.get_item(enter - 1).get_function_with_data(id_note)
        if action == -1:
            self.show_main_menu()

    def show_search_menu(self):
        self.search_menu.draw()
        values = [i + 1 for i in range(self.search_menu.len_items())]
        enter = self.__get_user_choice(values)
        action = self.search_menu.get_item(enter - 1).get_function()
        if action == -1:
            self.show_main_menu()

    def show_filter_notes_menu(self):
        self.filter_notes_menu.draw()
        values = [i + 1 for i in range(self.list_notes_menu.len_items())]
        enter = self.__get_user_choice(values)
        data = self.filter_notes_menu.get_item(enter - 1).get_data()
        action = self.filter_notes_menu.get_item(enter - 1).get_function_with_data(data)
        if action == -1:
            self.show_main_menu()

    def __get_user_choice(self, values):
        try:
            choice = int(input("Enter your choice: "))
            if choice not in values:
                raise ValueError
            else:
                os.system('cls||clear')
                return choice
        except ValueError:
            print('Incorrect value. Enter the number item menu. Please try again.')
            return self.__get_user_choice(values)

    def __exit(self, *args):
        return -1
