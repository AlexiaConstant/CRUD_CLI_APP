import sys
import unittest
import mysql.connector as connector
import mysql.connector.errors as errors
from src import msqlforapp
from src.msqlforapp import (
    mysqlconnect,
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


class TestCreateDrinks(unittest.TestCase):

   @classmethod
   def setUpClass(cls):
      db = mysqlconnect("")  # Open a connection to mysql (not any database)
      cursor = db.cursor()

      try:
         cursor.execute("CREATE DATABASE test")
      except Exception as e:
         print(f"Could not create database, {e}", file=sys.stdout)

      cursor.close()

      cursor = db.cursor()
      cursor.execute("CREATE TABLE IF NOT EXISTS test.drinks (id INT AUTO_INCREMENT PRIMARY KEY, drink_name VARCHAR(100), price DECIMAL(10,2))")
      cursor.close()
      db.close()

   @classmethod
   def tearDownClass(cls):
      db = mysqlconnect("")  # Open a connection to mysql (not any database)
      cursor = db.cursor()

      try:
         cursor.execute("DROP DATABASE test")
      except Exception as e:
         print(f"Could not drop database, {e}", file=sys.stdout)

      cursor.close()
      db.close()

   def test_create_drink(self):

      drink_name = ("Spring Water")
      price = ("1.50")
      insertVarintodrinks([(drink_name, price)], "test")
      result = print_drinks()
      row = result[-1]

      self.assertEqual(row[1], "Spring Water")
      self.assertEqual(float(row[2]), 1.50)

      db = mysqlconnect("test")
      cursor = db.cursor()
   
      sql_Delete_query = f"DELETE FROM drinks WHERE id = {row[0]}"
      cursor.execute(sql_Delete_query)
      db.commit()
      print("Record deleted successfully")

      cursor.close()
      db.close()
      print("MySQL connection is closed")


if __name__ == '__main__':
   unittest.main()