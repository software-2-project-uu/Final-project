import sqlite3 as db
from colorama import Fore
import datetime
from tabulate import tabulate

from part1_initDB import initDB
from part2_admin import startAdmin
from part3_cashier import startCashier

def getInt(s):
    while True:
        try:
            return int(input(s))
        except ValueError:
            print(Fore.RED + "Invalid input. Enter a number.")

def getPhone(s):
    while True:
        phone = input(s)
        if phone.isdigit() and len(phone) == 10:
            return phone
        else:
            print(Fore.RED + "Invalid phone number. Must be 10 digits.")

def main():
    while True:
        initDB()
        print("\n----------Shop Management----------")
        print("1 - Admin Login")
        print("2 - Cashier Login")
        print("0 - Shutdown")

        choice = getInt("\n\tEnter your choice: ")
        if choice == 1:
            startAdmin()
        elif choice == 2:
            startCashier()
        elif choice == 0:
            print("System shutting down...")
            break
        else:
            print(Fore.RED + "Invalid choice.")

if __name__ == "__main__":
    main()
