import tkinter as tk
from tkinter import *
import mysql.connector as connector
import mysql.connector.errors as errors

host = "localhost"
user = "root"
password = "password123"
port = "33066"

def mysqlconnect(database="app"):
    try:
        db_connection = connector.connect(
            host=host, user=user, password=password, port=port, database=database
        )
    except:
        print("Can't connect to database")
        exit()
    print("Connected")

    return db_connection


def prettyprintpeople():
    my_w = tk.Tk()
    my_w.geometry("300x200+10+10")
    my_w.title("List Of People")

    db = mysqlconnect()
    cursor = db.cursor()
    sql_faves = "SELECT people.id, people.first_name, people.last_name, drinks.drink_name from people LEFT JOIN drinks ON people.drink_id = drinks.id"
    cursor.execute(sql_faves)
    i = 0
    for people in cursor:
        for j in range(len(people)):
            e = Entry(my_w, width=10, fg="pink")
            e.grid(row=i, column=j)
            e.insert(END, people[j])
        i = i + 1

    my_w.mainloop()


def prettyprintdrinks():
    my_w = tk.Tk()
    my_w.geometry("300x200+10+10")
    my_w.title("List of Drinks")

    db = mysqlconnect()
    cursor = db.cursor()
    sql_faves = "SELECT * FROM drinks"
    cursor.execute(sql_faves)
    i = 0
    for people in cursor:
        for j in range(len(people)):
            e = Entry(my_w, width=10, fg="pink")
            e.grid(row=i, column=j)
            e.insert(END, people[j])
        i = i + 1

    my_w.mainloop()


def prettyprintpref():
    my_w = tk.Tk()
    my_w.geometry("300x200+10+10")
    my_w.title("List of Preferences")

    db = mysqlconnect()
    cursor = db.cursor()
    sql_faves = "SELECT people.id, people.first_name, people.last_name, drinks.drink_name from people LEFT JOIN drinks ON people.drink_id = drinks.id"
    cursor.execute(sql_faves)
    i = 0
    for people in cursor:
        for j in range(len(people)):
            e = Entry(my_w, width=10, fg="pink")
            e.grid(row=i, column=j)
            e.insert(END, people[j])
        i = i + 1

    my_w.mainloop()


def create_person():
    my_w = tk.Tk()
    my_w.geometry("400x300+10+10")
    my_w.title("Create Person")

    # label
    l0 = tk.Label(
        my_w, text="Create Person", font=("Helvetica", 16), width=30, anchor="c"
    )
    l0.grid(row=1, column=1, columnspan=4)
    l1 = tk.Label(my_w, text="First Name: ", width=10, anchor="c")
    l1.grid(row=3, column=1)

    # text box 1
    t1 = tk.Text(my_w, height=1, width=10, bg="white")
    t1.grid(row=3, column=2)
    l2 = tk.Label(my_w, text="Class: ", width=10)
    l2.grid(row=4, column=1)

    # text box 2
    t2 = tk.Text(my_w, height=1, width=10, bg="white")
    t2.grid(row=4, column=2)
    l3 = tk.Label(my_w, text="Last Name: ", width=10)
    l3.grid(row=4, column=1)

    # add record button
    b1 = tk.Button(my_w, text="Add Record", width=10, command=lambda: add_data())
    b1.grid(row=7, column=2)
    my_str = tk.StringVar()
    l4 = tk.Label(my_w, textvariable=my_str, width=10)
    l4.grid(row=3, column=3)
    my_str.set("Output")

    def add_data():
        flag_validation = True  # set the flag
        first_name = t1.get("1.0", END)  # read first name
        last_name = t2.get("1.0", END)  # read last name

        if len(first_name) < 2 and len(last_name) < 2:
            print("1")
            flag_validation = False

        print(type(first_name))
        print(type(last_name))

        try:
            _ = str(first_name)
            _ = str(last_name)
        except:
            print("2")
            flag_validation = False

        if flag_validation:
            my_str.set("Adding data...")

            try:
                db = mysqlconnect()

                cursor = db.cursor()
                query = "INSERT INTO people (first_name,last_name) VALUES (%s,%s)"

                my_data = (first_name, last_name)
                cursor.execute(query, my_data)  # insert data
                db.commit()

                cursor.close()
                db.close()

                t1.delete("1.0", END)  # reset the text entry box
                t2.delete("1.0", END)  # reset the text entry box
                l4.grid()
                l4.config(fg="green")  # foreground color
                l4.config(bg="white")  # background color
                my_str.set("id:" + str(id.lastrowid))
                l4.after(3000, lambda: l4.grid_remove())

            except Exception as e:
                error = str(e.__dict__["orig"])
                l4.grid()
                #return error
                l4.config(fg="red")  # foreground color
                l4.config(bg="yellow")  # background color
                print(error)
                my_str.set(error)

            finally:
                l4.grid()
                l4.config(fg="red")  # foreground color
                l4.config(bg="yellow")  # background color
                my_str.set("check inputs.")
                l4.after(3000, lambda: l4.grid_remove())

    my_w.mainloop()


def create_drinks():
    my_w = tk.Tk()
    my_w.geometry("400x300+10+10")
    my_w.title("Creprice")
    my_w.config(bg='pink')

    # label
    l0 = tk.Label(
        my_w, text="Create Drink", font=("Helvetica", 16), width=30, anchor="c"
    )
    l0.grid(row=1, column=1, columnspan=4)
    l0.config(bg='pink')
    l1 = tk.Label(my_w, text="Drink Name: ", width=10, anchor="c")
    l1.grid(row=3, column=1)
    l1.config(bg="LightPink1")

    # text box 1
    t1 = tk.Text(my_w, height=1, width=10, bg="white")
    t1.grid(row=3, column=2)
    l2 = tk.Label(my_w, text="Class: ", width=10)
    l2.grid(row=4, column=1)
    

    # text box 2
    t2 = tk.Text(my_w, height=1, width=10, bg="white")
    t2.grid(row=4, column=2)
    l3 = tk.Label(my_w, text="Drink Price: ", width=10)
    l3.grid(row=4, column=1)
    l3.config(bg="LightPink1")
    # add record button
    b1 = tk.Button(my_w, text="Add Record", width=10, command=lambda: add_data())
    b1.grid(row=7, column=2)
    my_str = tk.StringVar()
    l4 = tk.Label(my_w, textvariable=my_str, width=10)
    l4.grid(row=3, column=3)
    my_str.set("Output")

    def add_data():
        flag_validation = True  # set the flag
        first_name = t1.get("1.0", END)  # read first name
        price = t2.get("1.0", END)  # read last name

        if len(first_name) < 2 and len(price) < 1:
            print("1")
            flag_validation = False

        try:
            _ = str(first_name)
            _ = float(price)
        except:
            print("2")
            flag_validation = False

        if flag_validation:
            my_str.set("Adding data...")

            try:
                db = mysqlconnect()

                cursor = db.cursor()
                query = "INSERT INTO drinks (drink_name,price) VALUES (%s,%s)"

                my_data = (first_name, price)
                id = cursor.execute(query, my_data)  # insert data
                db.commit()

                cursor.close()
                db.close()

                t1.delete("1.0", END)  # reset the text entry box
                t2.delete("1.0", END)  # reset the text entry box
                l4.grid()
                l4.config(fg="green")  # foreground color
                l4.config(bg="white")  # background color
                #my_str.set("id:" + str(id.lastrowid))
                #l4.after(3000, lambda: l4.grid_remove())

            except Exception as e:
                #error = str(e.__dict__["orig"])
                l4.grid()
                #return error
                l4.config(fg="red")  # foreground color
                l4.config(bg="yellow")  # background color
                print(e)
                my_str.set(str(e))

            finally:
                l4.grid()
                l4.config(fg="red")  # foreground color
                l4.config(bg="yellow")  # background color
                my_str.set("check inputs.")
                l4.after(3000, lambda: l4.grid_remove())

    my_w.mainloop()

