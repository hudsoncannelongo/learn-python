import os 
import time
import black_market
import termcolor
os.system("clear")
user_name = input("Let's create a username for you: ")
account_password = input("Let's create a password for you: ")
print("Complete!!!")
time.sleep(3)

os.system("clear")
print("Welcome to Hudson's Blackmarket! But first we need to sign you in.")

score_count = 3

while score_count > 0:
    entered_username = input("What's the username: ")
    entered_password = input("What's the password: ")
    
    if user_name == entered_username and account_password == entered_password:
        print("You're done! You may begin shopping!")
        black_market.start_app ()
        break
    else:
        score_count -= 1
        print(f"Access denied. Try again. Attempts left: {score_count}")
        time.sleep(2)
        os.system("clear")
if score_count == 0:
    print("Too many failed attempts. Access permanently denied.")
    time.sleep(3)
    os.system('clear')
    
