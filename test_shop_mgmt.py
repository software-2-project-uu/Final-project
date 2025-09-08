# test_shop_mgmt.py
import unittest
from unittest.mock import patch
import sqlite3
import os

import part1_initDB
import part2_admin
import part3_cashier
import main  # replace with the actual filename where main() lives


class TestShopManagement(unittest.TestCase):

    def setUp(self):
        """Reset the database before each test"""
        if os.path.exists("shopMgmt.db"):
            os.remove("shopMgmt.db")
        part1_initDB.initDB()

    def tearDown(self):
        if os.path.exists("shopMgmt.db"):
            os.remove("shopMgmt.db")

    def get_conn(self):
        return sqlite3.connect("shopMgmt.db")

    def test_init_db_creates_tables(self):
        conn = self.get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = {row[0] for row in cursor.fetchall()}
        expected = {"users", "products", "purchaseHistory", "employees"}
        self.assertTrue(expected.issubset(tables))
        conn.close()

    # ----------------- LOGIN TESTS -----------------

    @patch("builtins.input", side_effect=["shopadmin", "admin123", "0"])
    def test_admin_login_success(self, mock_input):
        with patch("builtins.print") as mock_print:
            part2_admin.startAdmin()
            output = "".join([str(c[0]) for c in mock_print.call_args_list])
            self.assertIn("Login successful", output)

    @patch("builtins.input", side_effect=["wrong", "wrongpass"])
    def test_admin_login_fail(self, mock_input):
        with patch("builtins.print") as mock_print:
            part2_admin.startAdmin()
            output = "".join([str(c[0]) for c in mock_print.call_args_list])
            self.assertIn("Invalid admin credentials", output)

    @patch("builtins.input", side_effect=["cashier", "cash123", "0"])
    def test_cashier_login_success(self, mock_input):
        with patch("builtins.print") as mock_print:
            part3_cashier.startCashier()
            output = "".join([str(c[0]) for c in mock_print.call_args_list])
            self.assertIn("Login successful", output)

    @patch("builtins.input", side_effect=["cashier", "wrongpass"])
    def test_cashier_login_fail(self, mock_input):
        with patch("builtins.print") as mock_print:
            part3_cashier.startCashier()
            output = "".join([str(c[0]) for c in mock_print.call_args_list])
            self.assertIn("Invalid cashier credentials", output)

    # ----------------- INPUT VALIDATION -----------------

    @patch("builtins.input", side_effect=["123abc", "5", "0"])
    def test_getInt_validation(self, mock_input):
        with patch("builtins.print") as mock_print:
            result = main.getInt("Enter a number: ")
            self.assertEqual(result, 5)
            output = "".join([str(c[0]) for c in mock_print.call_args_list])
            self.assertIn("Invalid input", output)

    @patch("builtins.input", side_effect=["abcd", "12345", "9876543210"])
    def test_getPhone_validation(self, mock_input):
        with patch("builtins.print") as mock_print:
            result = main.getPhone("Enter phone: ")
            self.assertEqual(result, "9876543210")
            output = "".join([str(c[0]) for c in mock_print.call_args_list])
            self.assertIn("Invalid phone number", output)

    # ----------------- PRODUCT OPERATIONS -----------------

    @patch("builtins.input", side_effect=[
        "shopadmin", "admin123",  # login
        "3",  # Add/Update product
        "Apple", "10", "50",      # new product
        "0"   # Logout
    ])
    def test_admin_add_product(self, mock_input):
        part2_admin.startAdmin()

        conn = self.get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT productName, productPrice, productQty FROM products WHERE productName='Apple'")
        prod = cursor.fetchone()
        self.assertEqual(prod, ("Apple", 50, 10))
        conn.close()

    @patch("builtins.input", side_effect=[
        "shopadmin", "admin123",  # login
        "3", "Apple", "5",        # add qty to existing product
        "0"
    ])
    def test_admin_update_product_qty(self, mock_input):
        # Pre-insert product
        conn = self.get_conn()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO products (productName, productPrice, productQty) VALUES (?,?,?)", ("Apple", 50, 10))
        conn.commit()
        conn.close()

        part2_admin.startAdmin()

        conn = self.get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT productQty FROM products WHERE productName='Apple'")
        qty = cursor.fetchone()[0]
        self.assertEqual(qty, 15)  # 10 + 5
        conn.close()

    @patch("builtins.input", side_effect=[
        "cashier", "cash123",  # login
        "2",                   # Sell product
        "John Doe", "9876543210", "Apple", "2",
        "0"
    ])
    def test_cashier_sell_product(self, mock_input):
        # Pre-insert product
        conn = self.get_conn()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO products (productName, productPrice, productQty) VALUES (?,?,?)", ("Apple", 50, 10))
        conn.commit()
        conn.close()

        part3_cashier.startCashier()

        conn = self.get_conn()
        cursor = conn.cursor()
        # Product qty reduced
        cursor.execute("SELECT productQty FROM products WHERE productName='Apple'")
        qty = cursor.fetchone()[0]
        self.assertEqual(qty, 8)
        # Purchase history added
        cursor.execute("SELECT customerName, totalAmount FROM purchaseHistory WHERE customerName='John Doe'")
        record = cursor.fetchone()
        self.assertEqual(record[0], "John Doe")
        self.assertEqual(record[1], 100)  # 2 * 50
        conn.close()


if __name__ == "__main__":
    unittest.main()
