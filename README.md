A simple Shop Management System built with Python (SQLite3) for handling products, sales, employees, and user roles (Admin & Cashier).
Features:
1. Database Initialization (part1.py):
  Creates and initializes the SQLite database (shopMgmt.db).
  Tables:
    users → login credentials & roles
    products → product details & stock
    purchaseHistory → customer transactions
    employees → employee records
    Adds default users:
    Admin → shopadmin / admin123
    Cashier → cashier / cash123

2. Admin Panel (part2.py):
    Secure admin login.
    Menu options:
    View sales history
    View all products
    Add/update product quantity
    Update product price
    View employees
    Add new employees
    Change admin password
    Uses tabulate for clean table display.

3. Cashier Panel (part3.py):
    Secure cashier login.
    Menu options:
      View available products
      Sell products (with stock validation & purchase history logging)
      Change cashier password
      Automatically reduces stock after each sale.

4. Main Application (part4.py):
  Entry point of the system.
  Provides main menu:
  Admin login
    Cashier login
    Shutdown system
    Helper functions:
    getInt() → ensures numeric input
    getPhone() → ensures valid 10-digit phone number

Requirements:
Python 3.x
Libraries: colorama, tabulate
