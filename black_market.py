import os
import time
import termcolor
import pyttsx3

os.system("clear")
inventory = ["Cocaine", "Cigars", "Fentanyl", "Crystal Meth"]
cart = []
police_here = False


def display_cart():
    if cart:
        for item in cart:
            print(termcolor.colored(item, "yellow"))
    else:
        print("There is nothing in your cart!")


def display_inventory():
    if inventory:
        for item in inventory:
            print(termcolor.colored(item, "yellow"))
    else:
        print("sorry we ran out of all the illegal drugs 😁")


def browse_and_add():
    display_inventory()
    item = input(termcolor.colored("What would you like to buy? ", "green"))
    cart.append(item)


def check_first_item():
    if cart:
        print(f"The first item in your cart is: {cart[0]}")
    else:
        print("Your cart is empty!")


def remove_item():
    if not cart:
        print("Your cart is empty.")
        return
    item = input(f"What item would you like to remove from your cart {cart}? ")
    second_thoughts = input("Are you sure? Type 'yes' or 'no': ").lower()
    if second_thoughts == "yes":
        if item in cart:
            cart.remove(item)
            print(f"{item} has been removed from your cart.")
        else:
            print(f"{item} is not in your cart.")
    else:
        print("Okay, the item will remain in your cart.")


def clear_all():
    clear = input(
        "Would you like to clear every single cart item? Type 'yes' or 'no': "
    ).lower()
    if clear == "yes":
        cart.clear()
        print("Cart cleared.")
    else:
        print("Okay, I won't clear the cart.")


def self_destruct():
    os.system("clear")
    print(termcolor.colored("⚠️  SELF-DESTRUCT INITIATED ⚠️", "red", attrs=["bold"]))
    time.sleep(1)
    steps = [
        "Encrypting black market logs...",
        "Deleting evidence files...",
        "Wiping cartel database...",
        "Scrambling user identity...",
        "Detonating system core...",
    ]

    for step in steps:
        print(termcolor.colored(step, "yellow"))
        pyttsx3.speak(step)
        time.sleep(1.2)
    print(
        termcolor.colored("💥 SYSTEM SELF-DESTRUCT COMPLETE 💥", "red", attrs=["bold"])
    )
    time.sleep(2)
    print(termcolor.colored("Goodbye.", "cyan"))
    exit()  # ends the program


def start_app():
    print("Welcome to Hudson's Black Market! Now you may begin shopping.")
    time.sleep(2)
    os.system("clear")

    while True:
        time.sleep(1)
        os.system("clear")

        print("Type 'c'    - Check your cart")
        print("Type 'b'    - Browse inventory and add items")
        print("Type 'ci'   - Check the first item in your cart")
        print("Type 'ri'   - Remove an item from your cart")
        print("Type 'clr'  - Clear the entire cart")
        print("Type 'sd'   - 🔥 Self-Destruct Terminal")
        print("Type 'q'    - Quit the app")

        choice = (
            input(termcolor.colored("What's your choice: ", "blue")).strip().lower()
        )

        if choice == "c":
            display_cart()
        elif choice == "b":
            browse_and_add()
        elif choice == "ci":
            check_first_item()
        elif choice == "ri":
            remove_item()
        elif choice == "clr":
            clear_all()
        elif choice == "sd":
            self_destruct()
        elif choice == "q":
            print("Goodbye. Stay safe.")
            break
        else:
            print("Invalid input. Try again.")

        input("\nPress Enter to continue...")
