import os
import datetime

def get_time():
    now = datetime.datetime.now()
    return now.strftime("%a %H:%M")

def Seperator():
    print("-" * 30)

def print_menu():
    Seperator()
    print("Warehouse Management System      [" + get_time() + "]")
    Seperator()

    print("[1] Register New Item")
    print("[2] Display Catalog")
    print("[3] Update Item Stock")
    print("[4] Update Price")
    print("[5] Remove Item")
    print("[6] Display items out of stock")
    print("[7] Total Stock value")
    print("[8] List of categories")

    print("[x] Close")

def print_header(title):
    clear()
    Seperator()
    print(title)
    Seperator()
    
def clear():
    return os.system('cls')

def print_item(item):
    print(str(item.id).ljust(3) 
    + " | " + "Title: " + item.title.ljust(22) 
    + " | " + "Category: " + item.cat.ljust(22) 
    + " | " +"Price: $"+ str(item.price).ljust(10) 
    + " | " + "Stock: " +str(item.stock).ljust(10))
