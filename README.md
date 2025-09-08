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


<img width="1180" height="655" alt="185329085-eb5125d4-d608-4ffa-80f3-4812038431eb" src="https://github.com/user-attachments/assets/f8b7193e-2698-4f3f-bf36-580d693e130b" />
<img width="1168" height="687" alt="185329452-75747e33-3a59-4c15-baa1-df45073da916" src="https://github.com/user-attachments/assets/e4dd6583-e1e9-4fd4-be0d-828694fceff5" />
<img width="1110" height="837" alt="185332495-473cfccf-cebd-42bb-a875-46435c1968b5" src="https://github.com/user-attachments/assets/316194d4-022d-4a1a-be0a-e4cb4142ff30" />
<img width="977" height="882" alt="185333123-4283fd77-1540-4be9-9cbc-b8278a38a4f2" src="https://github.com/user-attachments/assets/18f84488-bb48-4c6c-ab16-c6a8ff5146d9" />
<img width="1101" height="807" alt="185333465-2f432a2c-2005-4414-92e5-b49c98b1deaf" src="https://github.com/user-attachments/assets/69441fa0-d5f6-42af-86c0-e4bb8b0f9ef6" />



