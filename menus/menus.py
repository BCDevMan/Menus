import os

from .menu_item import MenuItem


class Menus:
    def __init__(self, title=None, menu_items=None, help_text=None, return_on_valid_input=False, parent=None):
        """
            :param title (optional): The menu title displayed at the top of the menu.
            :param menu_items (optional): A list of menu items to be added at instantiation.
            (Can be added later using self.add_menu_item()
            :param help_text (optional): Help text displayed below the menu.
            :param return_on_valid_input (optional): If set to True, the menu will return to the parent menu whenever a valid input has been used.
            :param parent (optional): Allows you to set the parent menu, so you can interact with it from this menu
        """

        self.title = title
        self.help_text = help_text
        self.menu_items = {}
        if menu_items is not None:
            self.initialize_menu(menu_items=menu_items)
        self.parent: Menus = parent
        self.returned_values = None  # these are values returned by other menus, or functions to this menu.
        self.options = {}
        self.default_function = None
        self.return_on_valid_input = return_on_valid_input
        self.selected_key = None
        self.selected_menu_item = None
        self.prompt_text = "Please select an option: "
        self.message = ""
        self.set_default_options()

    def display_menu(self):
        while True:
            self.clear_screen()
            if self.title:
                print(self.title)
                self.separator()
            for item in self.menu_items.values():
                print(f'{self.get_key_option(item.key)} {item.text}')
            self.separator()
            if self.help_text:
                print(self.help_text)
                self.separator()
            if self.message:
                print(self.message)
                self.message = ""
                self.separator()
            try:
                self.get_input()
            except StopIteration:
                break

    @staticmethod
    def clear_screen():
        if os.name == 'nt':  # for windows
            os.system('cls')
        else:          # for mac and linux(here, os.name is 'posix')
            os.system('clear')

    def separator(self):
        print(self.options['separator']*self.options['sep_count'])

    def display(self, message):
        #  displays a message in the output area of the menu
        self.message = message

    def get_input(self):
        self.selected_key = input(self.prompt_text)
        if self.selected_key.lower() in self.menu_items:
            self.selected_menu_item = self.menu_items[self.selected_key]
            self.selected_menu_item()
            if self.return_on_valid_input:
                raise StopIteration('Stop on valid input')
        elif self.default_function:
            try:
                self.default_function(self)
            except TypeError:
                # This is to allow the user to create a callback function without parameters
                self.default_function()
        else:
            self.message = 'Invalid Menu Selection'

    def set_default_function(self, function):
        self.default_function = function

    def set_key_options(self, left='[', right=']'):
        self.options['key_left'] = left
        self.options['key_right'] = right

    def set_separator(self, separator='*', count=20):
        self.options['separator'] = separator
        self.options['sep_count'] = count

    def get_key_option(self, key):
        return f'{self.options["key_left"]}{key}{self.options["key_right"]}'

    def set_default_options(self):
        self.set_key_options()
        self.set_separator()

    def return_values(self, values):
        if self.parent is None:
            raise TypeError(f'Parent not Set for {self}')
        self.parent.returned_values = values

    def initialize_menu(self, menu_items):
        """
        :param menu_items: a list of lists
        [
            [menu_key1, menu_text1, menu_function1],
            [menu_key2, menu_text2, menu_function2],
            [menu_key3, menu_text3, menu_function3]
        ]
        :return: None, sets internal menu items
        """
        for menu_item in menu_items:
            self.add_menu_item(menu_item)

    def add_menu_item(self, menu_item):
        key, text, function = menu_item
        key = str(key)
        if key in self.menu_items:
            raise KeyError('Duplicate Menu Key')
        self.menu_items[key.lower()] = MenuItem(text=text, key=key, function=function, parent=self)
