import sqlite3 as db
from colorama import Fore
import datetime
from tabulate import tabulate

def startCashier():
    connectObj = db.connect("shopMgmt.db")
    cursor = connectObj.cursor()

    username = input("Enter cashier username: ")
    password = input("Enter cashier password: ")

    cursor.execute("SELECT * FROM users WHERE username=? AND password=? AND role='Cashier'", (username, password))
    row = cursor.fetchone()

    if row:
        print(Fore.GREEN + "Login successful. Welcome Cashier!")
        while True:
            print("\n--- Cashier Menu ---")
            print("1. View Products")
            print("2. Sell Product")
            print("3. Change Password")
            print("0. Logout")

            choice = input("Enter choice: ")

            if choice == "1":
                cursor.execute("SELECT * FROM products")
                rows = cursor.fetchall()
                print(tabulate(rows, headers=["ID", "Name", "Price", "Qty"]))
            
            elif choice == "2":
                cname = input("Enter customer name: ")
                phone = input("Enter phone number (10 digits): ")
                pname = input("Enter product name: ")
                qty = int(input("Enter quantity: "))

                cursor.execute("SELECT * FROM products WHERE productName=?", (pname,))
                prod = cursor.fetchone()
                if prod and prod[3] >= qty:
                    total = qty * prod[2]
                    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    cursor.execute("INSERT INTO purchaseHistory (customerName, phoneNumber, productName, qty, totalAmount, purchaseDate) VALUES (?,?,?,?,?,?)", 
                                   (cname, phone, pname, qty, total, date))
                    cursor.execute("UPDATE products SET productQty = productQty - ? WHERE productName=?", (qty, pname))
                    connectObj.commit()
                    print(Fore.GREEN + f"Purchase successful. Total = {total}")
                else:
                    print(Fore.RED + "Not enough stock or product not found.")
            
            elif choice == "3":
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
        print(Fore.RED + "Invalid cashier credentials.")

    connectObj.close()

