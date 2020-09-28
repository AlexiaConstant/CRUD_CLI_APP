import os
import tkinter  as tk 
from tkinter import *
import mysql.connector as connector
import mysql.connector.errors as errors
from src.guites import prettyprintpeople, prettyprintdrinks,prettyprintpref,create_person,create_drinks
from src.msqlforapp import (
    create_table_people,
    create_table_drinks,
    insertVarintopeople,
    insertVarintodrinks,
    joining_drink_people,
    update_favorite_drink,
    print_people,
    print_drinks,
    delete_people,
    delete_drink,
)
from src.models.models import new_person

menu = """

Please choose an option:

[1] List All People
[2] List All Drinks
[3] List All Preferences
[4] Create Person
[5] Create Drink
[6] Delete Person
[7] Delete Drink
[8] Create Preference
[0] Exit

"""
exit_option = 0
# prefs = get_data(Strategy.preferences)

def app():
    while True:

        option = None

        try:

            option = int(input(menu))
        except ValueError:

            print("Please enter a number")

        if option == exit_option:

            break
        elif option == 1:
            prettyprintpeople()

        elif option == 2:
            prettyprintdrinks()

        elif option == 3:
            prettyprintpref()

        elif option == 4:
            create_person()
            
        elif option == 5:
            create_drinks()


        elif option == 6:
            print_people()
            people_ques = input("Please input the ID of the Person you would like to delete:")
            delete_people(people_ques)

        elif option == 7:
            print_drinks()
            drink_ques = input("Please enter the ID of the drink you would like to delete:")
            delete_drink(drink_ques)

        elif option == 8:
            print_people()
            person_id = input("Please input Person ID")
            print_drinks()
            drink_id = input("Please input Drink ID")
            update_favorite_drink(person_id,drink_id)

if __name__ == "__main__":
    app()