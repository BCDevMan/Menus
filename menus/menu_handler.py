import os

from .menu_item import MenuItem


class Menus:
    def __init__(self, title=None, help_text=None, menu_items=None):
        """
        Class for construction of a basic CLI menu
        A menu with default options enabled will appear as:

            Menu Title
            ********************
            [key] menu item
            [key] menu item
            [key] menu item
            ********************
            Help Text
            ********************
            Output / Messages
            ********************
            prompt:

        :param title: The menu title displayed at the top of the menu (optional)
        :param help_text: Help text displayed below the menu (optional)
        :param menu_items: A list of menu items to be added at instantiation
            (Can be added later using self.add_menu_item()

        Adding Menu Items
            menu_item is a list containing the following: [key, text, callback function]
                key: The key you wish to press to select that menu item (case insensitive, must be unique per menu)
                text: the text you want displayed in the menu
                callback function: the function you wish to have called when that menu item is selected
                    NOTES:
                        If the callback is set to None, it will exit this menu when that item is selected, and return
                        to the previous menu.
                        Any callback function can take a single parameter which is the menu object.
                        this allows you to access menu fields and methods from within the callback function.
                        most commonly menu.display("Text to be displayed")
                        and menu.selection_text  (This contains a copy of what the user entered at the prompt)
                        you can also access menu.selection_item, which contains a copy of the menu item that
                        was selected.

        Options:
            set_default_function(self, function):
                This sets a callback function to be called if text is entered that is not a menu key.
            set_key_options(self, left='[', right=']'):
                This allows you to change the enclosures displayed around the key.
                NOTE: If you only want a single enclosure such as 1). must set the opposite enclosure to an empty
                string.
                    Example: menu.set_key_options(left="", right=")."
            set_separator(self, separator='*', count=20):
                This sets the type and length of the line used to separate parts of the menu.
            prompt_text:
                This is the text displayed by the prompt
        """

        self.title = title
        self.help_text = help_text
        self.menu_items = {}
        if menu_items is not None:
            self.initialize_menu(menu_items=menu_items)
        self.options = {}
        self.default_function = None
        self.selection_item = None
        self.selection_text = None
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
        response = input(self.prompt_text)
        if response.lower() in self.menu_items:
            self.selection_item = self.menu_items[response]
            self.selection_item()
        elif self.default_function:
            self.selection_text = response
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

