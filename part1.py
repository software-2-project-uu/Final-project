import sqlite3 as db
from colorama import Fore
import datetime
from tabulate import tabulate

def initDB():
    connectObj = db.connect("shopMgmt.db")
    cursor = connectObj.cursor()

    # جدول کاربران
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        username TEXT PRIMARY KEY,
                        password TEXT NOT NULL,
                        role TEXT NOT NULL)''')

    # جدول محصولات
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                        productId INTEGER PRIMARY KEY AUTOINCREMENT,
                        productName TEXT,
                        productPrice INTEGER,
                        productQty INTEGER)''')

    # جدول تاریخچه خرید
    cursor.execute('''CREATE TABLE IF NOT EXISTS purchaseHistory (
                        purchaseId INTEGER PRIMARY KEY AUTOINCREMENT,
                        customerName TEXT,
                        phoneNumber TEXT,
                        productName TEXT,
                        qty INTEGER,
                        totalAmount INTEGER,
                        purchaseDate TEXT)''')

    # جدول کارمندان
    cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                        empId INTEGER PRIMARY KEY AUTOINCREMENT,
                        empName TEXT,
                        empRole TEXT)''')

    # افزودن کاربران پیش‌فرض
    cursor.execute("INSERT OR IGNORE INTO users VALUES ('shopadmin','admin123','Admin')")
    cursor.execute("INSERT OR IGNORE INTO users VALUES ('cashier','cash123','Cashier')")

    connectObj.commit()
    connectObj.close()

print("Database initialized successfully.")
