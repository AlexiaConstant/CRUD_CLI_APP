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


def create_database():
    db = mysqlconnect("")  # Open a connection to mysql (not any database)
    cursor = db.cursor()

    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS app")
        # TODO Is always called...
        print("app database has been created")
    except Exception as e:
        print("Could not create database")
        print(e)

    cursor.close()
    db.close()


def create_table_people():
    db = mysqlconnect()
    cursor = db.cursor()
    # cursor.execute("DROP TABLE IF EXISTS people")
    sql_people = "CREATE TABLE IF NOT EXISTS people (id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(50), last_name VARCHAR(100), drink_id INT, FOREIGN KEY (drink_id) REFERENCES drinks(id) ON DELETE SET NULL)"
    cursor.execute(sql_people)
    cursor.close()
    db.close()


def create_table_drinks():
    db = mysqlconnect()
    cursor = db.cursor()
    # cursor.execute("DROP TABLE IF EXISTS people")
    sql_drinks = "CREATE TABLE IF NOT EXISTS drinks (id INT AUTO_INCREMENT PRIMARY KEY, drink_name VARCHAR(100), price DECIMAL(10,2))"
    cursor.execute(sql_drinks)
    cursor.close()
    db.close()


def insertVarintopeople(my_vars):  # [("first_name", "surname")]
    db = mysqlconnect()
    cursor = db.cursor()
    try:
        query = "INSERT INTO people (first_name,last_name) VALUES (%s,%s)"
        # query_vals = [(" Alexia","Con"), ("Manny", "Lowmax"),("Katie","Gillmore"),
        #        ("Anna","Sherman"),("Billy","Jiglla")]
        cursor.executemany(query, my_vars)
        db.commit()
        print(cursor.rowcount, "record inseted")

    except Exception as e:
        print("Failed to insert into MySQL table {}".format(e))

    finally:
        if db.is_connected():
            cursor.close()
            db.close()
            print("MySQL connection is closed")


""" class Print_Table:
    def __init__(self, table,db,cursor,results):
        self.table = table
        self.db = mysqlconnect()
        self.cursor = cursor.execute("SELECT * FROM people")
        self.results = cursor.fetchall()

    def __str__(self):
        return self.results
"""
# TODO CLEANUP like delete_drink
def delete_people(id):
    try:
        db = mysqlconnect()
        cursor = db.cursor()
        sql_Delete_query = "DELETE FROM people WHERE id = %s"
        # peopleId = 2
        cursor.execute(sql_Delete_query, (id,))
        db.commit()
        print("Record deleted successfully")

    except Exception as e:
        print("Failed to Delete record from table: {}".format(e))

    finally:
        if db.is_connected():
            cursor.close()
            db.close()
            print("MySQL connection is closed")


def delete_drink(id):
    try:
        db = mysqlconnect()
        cursor = db.cursor()
        sql_Delete_query = "DELETE FROM drinks WHERE id = %s"
        # drinkId = 2
        cursor.execute(sql_Delete_query, (id,))
        db.commit()
        print("Record deleted successfully")

    except Exception as e:
        print("Failed to Delete record from table: {}".format(e))

    finally:
        if db.is_connected():
            cursor.close()
            db.close()
            print("MySQL connection is closed")


def print_people():
    db = mysqlconnect()
    cursor = db.cursor()
    sql_faves = "SELECT people.id, people.first_name, people.last_name, drinks.drink_name from people LEFT JOIN drinks ON people.drink_id = drinks.id"
    cursor.execute(sql_faves)
    # cursor.execute("SELECT * FROM people")
    results = cursor.fetchall()

    for x in results:
        print(x)

    cursor.close
    db.close()
    print("MySQL connection is closed")


def print_drinks():
    db = mysqlconnect()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM drinks")
    results = cursor.fetchall()

    for x in results:
        print(x)

    cursor.close
    db.close()
    print("MySQL connection is closed")


def insertVarintodrinks(my_vars):
    db = mysqlconnect()
    cursor = db.cursor()
    try:
        query = "INSERT INTO drinks (drink_name,price) VALUES (%s,%s)"
        # query_vals = [("Hot Coco","1.59"), ("Fanta", "2.00"),("Martini","5.00"),
        #        ("Hot Toddy","4.50")]
        cursor.executemany(query, my_vars)
        db.commit()
        print(cursor.rowcount, "record inseted")

    except Exception as e:
        print("Failed to insert into MySQL table {}".format(e))

    finally:
        if db.is_connected():
            cursor.close()
            db.close()
            print("MySQL connection is closed")


def joining_drink_people():
    db = mysqlconnect()
    cursor = db.cursor()
    # cursor.execute("DROP TABLE IF EXISTS people")
    sql_faves = "SELECT people.id, people.first_name, people.last_name, drinks.drink_name from people LEFT JOIN drinks ON people.drink_id = drinks.id"
    cursor.execute(sql_faves)
    results = cursor.fetchall()
    print(results)
    cursor.close()
    db.close()


def update_favorite_drink(person_id, drink_id):
    db = mysqlconnect()
    cursor = db.cursor()
    query = "UPDATE people SET drink_id = %s WHERE people.id = %s"

    cursor.execute(query, (drink_id, person_id))
    db.commit()

    cursor.close()
    db.close()


# def round_drinks():
#     db=mysqlconnect()
#     cursor = db.cursor()
#         try:
#             query = ""
#         query = "INSERT INTO rounds SELECT FROM people (first_name) SELECT FROM drinks (drink_name,price) VALUES (%s,%s,%s)"
#         #sum_it = "SELECT SUM price AS totalsum FROM drinks"
#         cursor.executemany(query, sum_it, my_vars)
#         result = cursor.fetchall()

#         for i in result:
#             print(i[0])

#         if(db.is_connected()):
#             cursor.close()
#             db.close()
#             print("MySQL connection is closed")


if __name__ == "__main__":
    pass
    # insertVarintopeople()
    # round_drinks()
    # delete_drink(2)
    # delete_people(3)
