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


class TestCreatePerson(unittest.TestCase):
   def test_create_people(self):
      db = mysqlconnect()
      cursor = db.cursor()
#Act 
      first_name = ("Billy")
      last_name = ("Rider")
      insertVarintopeople([(first_name, last_name)])
      result = print_people()
      row = result[4]

#assert
      self.assertEqual(row[1], "Billy")
      self.assertEqual(row[2], "Rider")
   
      sql_Delete_query = f"DELETE FROM people WHERE id = {row[0]}"
      cursor.execute(sql_Delete_query)
      db.commit()
      print("Record deleted successfully")

      cursor.close()
      db.close()
      print("MySQL connection is closed")


if __name__ == '__main__':
   unittest.main()
