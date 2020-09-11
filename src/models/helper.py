import os
from classes import Strategy

def clear_screen():
    os.system("clear")


def print_list(strategy: Strategy, some_list):
    clear_screen()
    title = None
    if strategy == Strategy.people:
        title = "People"
    elif strategy == Strategy.drinks:
        title = "Drinks"
    elif strategy == Strategy.preferences:
        title = "Preferences"
    print(title.upper())
    print('-'*30)
    for key, item in enumerate(some_list):
        print("\t", f"{key}, {item}")


# def print_prefs(prefs):
#     clear_screen()
#     print("PREFERENCES")
#     print('-'*30)
#     for pref in prefs.values():
#         print(pref)


def read_lines(file_name):
    try:
        the_file = open(file_name, "r")
        lines = the_file.readlines()
    except:
        return []
    return lines


def write_list(file_name, the_list, prop):
    try:
        the_file = open(file_name, "w")

        for item in the_list:
            the_file.write(getattr(item, prop) + "\n")
    finally:
        the_file.close()
