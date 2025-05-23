import os

import time

os.system("clear")

print("Welcome to Huddies black market")

inventory = ["shot gun", "lost dog", "pistol", "drugs", "baobao"]
cart = []


def add_item():
    print(f"Here is the inventory: {inventory}")
    item = input("What would you like to illegally buy!: ")

    if item in inventory:
        cart.append(item)
        print("Good doin' illegal business with ya!")
    else:
        print("Yo tryin' to buy somtin dat ain't here dude!  Yo cra cra")


def view_list():
    print(cart)


def show_firstitem():
    print(f"this is your first item { cart[0] }")


def remove_first_item():
    cart.pop(0)
    print("your first item has been removed")


def remove_item():
    item_to_remove = input("What do you want to remove: ")
    if item_to_remove in cart:
        cart.remove(item_to_remove)
        print(f"your {item_to_remove} has been removed")
    else:
        print("That item is not in your cart dummy!")

    while True:
        print("Type a to add")
        print("Type e to exit")
        print("Type f to show the first item")
        print("Type rmf to remove the first item from the list")
        print("Type rm to remove a certain item")
        print("type v to view your list")

        choice = input("What do you want to do?: ")
        if choice == "a":
            add_item()
        elif choice == "v":
            view_list()
        elif choice == "f":
            show_firstitem()
        elif choice == "rmf":
            remove_first_item()
        elif choice == "rm":
            remove_item()
        elif choice == "e":
            break

        time.sleep(3)
        os.system("clear")


print("Gooooooood bye")
