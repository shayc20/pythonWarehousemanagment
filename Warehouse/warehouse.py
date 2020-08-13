"""
        Program: Warehouse Management System
        Author: Shamus Cerny
Description: 
1 - Register New Item
        id(auto gen)
        title(str)
        category(str)
        price(float)
        stock(int)
2- display catalog
3- update stock
4- Remove item from catalog
5- print total stock value
6- Report- item out of stock
"""

# imports
from menu import clear, print_menu, print_header, print_item
from item import Item
import pickle



# Global Var
catalog = []
data_file = 'Warehouse.data'

def serialize_catalog():
    global data_file
    writer = open(data_file, 'wb') # Create/open a file to write binary
    pickle.dump(catalog, writer)
    writer.close() # Close Stream and release the file
    print("** Data Serialized!")

def deserialize_catalog():
    try:
        global data_file
        reader = open(data_file, 'rb')#Open file to read binary
        temp_list = pickle.load(reader)
    
        for item in temp_list:
            catalog.append(item)

        print("** Deserialized " + str(len(catalog)) + " Items" )
    
    except:
        print("Error, could not load data")

# Fn
def Register():
    try:
        print_header("Register New Item")
        title = str(input("Please provide a Title: "))
        cat = str(input("Please provide the Category: "))
        price = float(input("Please provide the Price: "))
        stock = int(input("Please provide the amount of Stock: "))
        value = float

        id = 1
        item = Item(id, title, cat, price, stock)
        catalog.append(item)

        how_many = len(catalog)
        print("you now have: " + str(how_many) + " items on the catalog")
    except ValueError:
        print("Error, you have entered an invalid character")
    except:
        print("Error, Something went wrong")

def display_catalog():
    print_header("Your Current Catalog")
    # Travel the list
    for item in catalog:
        print_item(item)

def display_out_of_stock():
    print_header("Items Currently out of stock")
    for item in catalog:
        if(item.stock == 0):
            print_item(item)

def display_value():
    print_header("Here are the total values of each item")
    total = 0.0
    for item in catalog:
        value = (item.price * item.stock)
        total += value

        print(str(item.id).ljust(3) + " | " + "Title: " + item.title.ljust(22) + " | " + "Value: " + str(value))
    print(" The Total value of Warehouse: $" + str(total))

def display_catagories():
    category = []
    num = 0
    print_header("Catagories")
    for item in catalog:
        if item.cat not in category:
            category.append(item.cat)
    for item in category:
        num += 1
        print(" Category "+ str(num) + item.rjust(20))


#  Instructions
deserialize_catalog()
input("Press enter to continue...")

opc = ''
while(opc != "x"):
    print_menu()

    opc = input("Please choose an option: ")
    #  If comparisons
    if(opc == '1'):
        Register()
        serialize_catalog()
    elif(opc == '2'):
        display_catalog()
    elif(opc =='6'):
        display_out_of_stock()
    elif(opc =='7'):
        display_value()
    elif(opc =='8'):
        display_catagories()

    input("Press enter to continue...")
    clear()

    if(opc == 'x'):
        clear()