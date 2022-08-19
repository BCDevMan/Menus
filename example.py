import sys
from menus import Menus


def main():
    menu = Menus('Main Menu', menu_items=[
        ['1', 'Hello', hello],
        ['2', 'Goodbye', goodbye],
        ['3', 'Sub Menu', sub_menu],
        ['4', 'Auto Menu', auto_menu],
        ['6', 'Auto Return', return_menu],
        [7, 'Menu with returned value', get_returned]
    ])
    menu.add_menu_item(['0', 'Exit Program', exit_program])
    menu.display_menu()


def get_returned(menu):
    returning_menu(menu)
    menu.display(menu.returned_values)


def returning_menu(parent):
    ret_menu = Menus('Return an input', [
        [1, 'Get Input', get_input],
        [2, 'Exit', None]
    ], parent=parent)
    ret_menu.return_on_valid_input = True
    ret_menu.display_menu()

def get_input(menu):
    response = input('Enter something')
    menu.parent.returned_values = response

def sub_menu():
    menu = Menus('Sub Menu', menu_items=[
        ['A', "Hello", sub_hello],
        ['B', "Good Bye", sub_bye],
        ['X', 'Back to Main Menu', None],
        ['XXX', 'Exit Program', exit_program],
    ], help_text='Press any option key, or enter \nanything that is not a key to print that.')
    menu.set_separator('-', 50)
    menu.set_key_options('<', '>:')
    menu.set_default_function(defaulter)
    menu.display_menu()


def auto_menu():
    items = ('aaaa', 'bbbb', 'ccccc')
    menu = Menus('Auto')
    for key, item in enumerate(items, 1):
        menu.add_menu_item([key, item, auto_func])
    menu.add_menu_item([len(items)+1, 'Main Menu', None])
    menu.set_key_options(left='', right=').')
    menu.set_default_function(defaulter)
    menu.prompt_text = "Please select an option\n" \
                       "Or type anything to print: "
    menu.display_menu()


def return_menu():
    menu = Menus('Return after valid input', menu_items=[
        ['1', 'Test1', return_menu_feedback],
        ['2', 'Testings', return_menu_feedback],
        [3, 'Exit', None]
    ])
    menu.return_on_valid_input = True
    menu.display_menu()


def return_menu_feedback(menu: Menus):
    print(menu.selected_menu_item.text)


def auto_func(menu):
    menu.display(menu.selected_menu_item.text)


def exit_program():
    sys.exit()


def sub_hello(menu):
    menu.display('Sub Menu Says Hello!')


def sub_bye(menu):
    menu.display('Sub Menu Says Goodbye!')


def hello(menu):
    menu.display('Hello')


def goodbye(menu):
    menu.display('Auf Wiedersehen')


def defaulter(menu):
    menu.display(menu.selected_key)


if __name__ == "__main__":
    main()
