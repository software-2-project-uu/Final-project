import sqlite3 as db
from colorama import Fore
import datetime
from tabulate import tabulate

def startAdmin():
    connectObj = db.connect("shopMgmt.db")
    cursor = connectObj.cursor()

    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    cursor.execute("SELECT * FROM users WHERE username=? AND password=? AND role='Admin'", (username, password))
    row = cursor.fetchone()

    if row:
        print(Fore.GREEN + "Login successful. Welcome Admin!")
        while True:
            print("\n--- Admin Menu ---")
            print("1. View Sales")
            print("2. View Products")
            print("3. Add/Update Product Quantity")
            print("4. Update Product Price")
            print("5. View Employees")
            print("6. Add Employee")
            print("7. Change Password")
            print("0. Logout")

            choice = input("Enter choice: ")

            if choice == "1":
                cursor.execute("SELECT * FROM purchaseHistory")
                rows = cursor.fetchall()
                print(tabulate(rows, headers=["ID", "Customer", "Phone", "Product", "Qty", "Total", "Date"]))
            
            elif choice == "2":
                cursor.execute("SELECT * FROM products")
                rows = cursor.fetchall()
                print(tabulate(rows, headers=["ID", "Name", "Price", "Qty"]))
            
            elif choice == "3":
                name = input("Enter product name: ")
                qty = int(input("Enter qty: "))
                cursor.execute("SELECT * FROM products WHERE productName=?", (name,))
                if cursor.fetchone():
                    cursor.execute("UPDATE products SET productQty = productQty + ? WHERE productName=?", (qty, name))
                else:
                    price = int(input("Enter price: "))
                    cursor.execute("INSERT INTO products (productName, productPrice, productQty) VALUES (?,?,?)", (name, price, qty))
                connectObj.commit()
                print(Fore.GREEN + "Product added/updated successfully.")
            
            elif choice == "4":
                name = input("Enter product name: ")
                price = int(input("Enter new price: "))
                cursor.execute("UPDATE products SET productPrice=? WHERE productName=?", (price, name))
                connectObj.commit()
                print(Fore.GREEN + "Price updated.")
            
            elif choice == "5":
                cursor.execute("SELECT * FROM employees")
                rows = cursor.fetchall()
                print(tabulate(rows, headers=["ID", "Name", "Role"]))
            
            elif choice == "6":
                empName = input("Enter employee name: ")
                empRole = input("Enter role: ")
                cursor.execute("INSERT INTO employees (empName, empRole) VALUES (?,?)", (empName, empRole))
                connectObj.commit()
                print(Fore.GREEN + "Employee added.")
            
            elif choice == "7":
                newPass = input("Enter new password: ")
                cursor.execute("UPDATE users SET password=? WHERE username=?", (newPass, username))
                connectObj.commit()
                print(Fore.GREEN + "Password changed.")
            
            elif choice == "0":
                print("Logged out.")
                break
            
            else:
                print(Fore.RED + "Invalid choice.")
    else:
        print(Fore.RED + "Invalid admin credentials.")

    connectObj.close()
