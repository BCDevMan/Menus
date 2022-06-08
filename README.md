# Menus
Basic CLI Menu Service for Python
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

usage:
menu = Menu(title="Menu Title", help_text="Menu Help Text", menu_items=[
        ['A', 'Menu item 1', callback_function_1],
        ['B', 'Menu item 2', callback_function 2],
        ['C', 'Back to previous menu', None],
        ['X', 'Exit Program, exit_program],
      ])
menu.display_menu()

        :param title (optional): The menu title displayed at the top of the menu.
        :param help_text (optional): Help text displayed below the menu.
        :param menu_items (optional): A list of menu items to be added at instantiation.
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
               
Please see example.py for a working example with all options used.
