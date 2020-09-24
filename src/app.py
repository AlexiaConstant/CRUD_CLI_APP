import os

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


while True:

    option = None

    try:

        option = int(input(menu))
    except ValueError:

        print("Please enter a number")

    if option == exit_option:

        break
    elif option == 1:
        print_people()

    elif option == 2:
        print_drinks()

    elif option == 3:
        joining_drink_people()

    elif option == 4:
        first_name = input("Please input first name:")
        last_name = input("Please input last name:")
        insertVarintopeople([(first_name, last_name)])

    elif option == 5:
        drink_name = input("Please input drink name:")
        price = input("Please input drink price:")
        insertVarintodrinks([(drink_name, price)])

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

