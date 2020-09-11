import os
import csv
from classes import Drink, Person, Preference, Round, Strategy
from helpers import read_lines, write_list, clear_screen, print_list
from csv import reader


def get_data(strategy: Strategy):
    filename = None
    if strategy == Strategy.people:
        filename = "names"
    elif strategy == Strategy.drinks:
        filename = "drinks"
    elif strategy == Strategy.preferences:
        filename = "preferences"
    data = []
    with open(f"{filename}.csv", "r") as the_file:
        reader = csv.reader(the_file)

        for key, row in enumerate(reader):
            info = None
            if strategy == Strategy.people:
                info = Person(key, row[0])
            elif strategy == Strategy.drinks:
                info = Drink(key, row[0])
            elif strategy == Strategy.preferences:
                info = Preference(people[int(row[0])], drinks[int(row[1])])
            data.append(info)

    return data


def get_drinks():
    lines = read_lines("drinks.txt")
    data = []
    for line in lines:
        data.append(Drink(line.strip()))
    return data

def write_data(filename, data):
    with open(filename,'w') as file:
        for line in data:
            file.write(str(line))
            file.write('\n')

def write_prefs(filename):
    with open(filename,'w') as file:
        for pref in prefs:
            file.write(f"{pref.person.id}, {pref.drink.id}")
            file.write('\n')

def save(strategy: Strategy):
    filename = None
    data = None
    if strategy == Strategy.people:
        write_data(f"names.csv", people)
    elif strategy == Strategy.drinks:
        write_data(f"drinks.csv", drinks)
    elif strategy == Strategy.preferences:
        write_prefs("preferences.csv")



def save_and_exit():
    save(Strategy.people)
    save(Strategy.drinks)
    exit()


def create(strategy: Strategy, data):
    if strategy == Strategy.people:
        people.append(data)
    elif strategy == Strategy.drinks:
        drinks.append(data)
    elif strategy == Strategy.preferences:
        prefs.append(data)
    save(strategy)


def create_drink(name: str):
    new_drink = Drink(name)
    drinks.append(new_drink)


def create_pref(person: Person, drink: Drink):
    new_dict_item = {person.name: Preference(person, drink)}
    prefs.update(new_dict_item)


menu = """
Please choose an option:

[1] List All People
[2] List All Drinks
[3] List All Preferences
[4] Create Person
[5] Create Drink
[6] Create Preference
[0] Exit

"""
exit_option = 0
people = get_data(Strategy.people)
drinks = get_data(Strategy.drinks)
prefs = get_data(Strategy.preferences)


while True:


    option = None

    try:

        option = int(input(menu))
    except ValueError:

        print('Please enter a number')

    if option == exit_option:
        
        break
    elif option == 1:
        print_list(Strategy.people, people)
    elif option == 2:
        print_list(Strategy.drinks, drinks)
    elif option == 3:
        print_list(Strategy.preferences, prefs) 
    elif option == 4:
        create(Strategy.people, Person(len(people), input("Please enter person: ")))
    elif option == 5:
        create(Strategy.drinks, Drink(len(drinks), input("Please enter drink: ")))
   
    elif option == 6:
        selected_person = None
        selected_drink = None

        print_list(Strategy.people, people)
        while selected_person == None:
            try:
                person_idx = int(input("Please choose a person: "))
                selected_person = people[person_idx]
            except:
                print("Invalid choice...")

        print_list(Strategy.drinks, drinks)
        while selected_drink == None:
            try:
                drink_idx = int(input("Please choose a drink: "))
                selected_drink = drinks[drink_idx]
            except:
                print("Invalid choice...")

        create(Strategy.preferences, Preference(selected_person, selected_drink))


save_and_exit()
