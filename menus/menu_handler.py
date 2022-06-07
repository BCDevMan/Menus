import os

from .menu_item import MenuItem


class Menus:
    def __init__(self, title=None, help_text=None, menu_items=None):
        self.title = title
        self.help_text = help_text
        self.menu_items = {}
        if menu_items is not None:
            self.initialize_menu(menu_items=menu_items)
        self.options = None
        self.valid_options = None
        self.set_default_options()
        self.message = ""

    def display_menu(self):
        while True:
            self.clear_screen()
            print(self.title)
            self.separator()
            for item in self.menu_items.values():
                print(f'{item.key} {item.text}')
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
        print(self.options['separator']*20)

    def print_out(self, message):
        self.message = message

    def get_input(self):
        response = input('Please enter an options: ').lower()
        if response in self.menu_items:
            self.menu_items[response]()
        else:
            self.message = 'Invalid Menu Selection'

    def add_menu_item(self, menu_item):
        key, text, function = menu_item
        self.menu_items[key.lower()] = MenuItem(text=text, key=key, function=function, parent=self)

    # def remove_menu_item(self, menu_key):
    #     pass
    #
    # def edit_menu_item(self, menu_key):
    #     pass

    def change_menu_options(self, key, value):
        if key in self.options:
            self.options[key] = value
        else:
            raise KeyError('Invalid Options Key')

    def key_option(self, key):
        if self.options['key_options'] == 'brackets':
            return f'[{key}]'
        elif self.options['key_options'] == 'parens':
            return f'({key})'
        elif self.options['key_options'] == 'angles':
            return f'<{key}>'
        elif self.options['key_options'] == 'bars':
            return f'|{key}|'
        elif self.options['key_options'] == 'colon':
            return f'{key}:'
        elif self.options['key_options'] == 'period':
            return f'{key}.'
        elif self.options['key_options'] == 'parens_period':
            return f'{key}).'
        elif self.options['key_options'] is None:
            return f'{self.options["key_options_begin"]}{key}{self.options["key_options_end"]}'

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

    def set_default_options(self):
        self.options = {
            'separator': '*',
            'key_options': 'brackets',
            'key_options_begin': '[',
            'key_options_end': ']'
        }

        self.valid_options = {
        }
