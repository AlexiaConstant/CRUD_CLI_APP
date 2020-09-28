import unittest
from unittest import mock
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


class TestAppMenu(unittest.TestCase):
   @mock.patch("src.app.prettyprintpeople")
   @mock.patch("builtins.input", side_effect=["1", "0"])
   def test_print_people(self, mock_input, mock_ppp):
      from src.app import app

      app()

      self.assertEqual(mock_input.call_count, 2)
      mock_ppp.assert_called_once()

if __name__ == '__main__':
   unittest.main()