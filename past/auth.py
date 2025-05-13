
# 1. Ask the user to create a username and store it in a variable

# 2. Ask the user to create a password and store it in a variable
# 3. Ask the user to create a password hint and store it in a variable

# 4. Clear the screen: os.system('clear')


# 5. Ask the user to log in by typing their username and store it in a variable
# 6. Ask the user to type their password and store it in a variable

# 7.- Check if the entered username matches the saved username
#   - IF SO then check if the password matches
#        - IF the password is correct
#           - print a success message
#     - ELSE, the password is wrong, offer to show the password hint
#        - IF the user says yes
#           - display the password hint
#   - ELSE, the username doesn't match
#      - print an error message


import os
from termcolor import colored

os.system ('clear')

user_name = input (" Creat a username: ")

password = input (" Creat a Password: ")

hint_password = input("Create a password hint: ")

print("Your password hint has been saved.")

os.system('clear') 

enterd_username = input (" please enter your username: ")

if user_name == enterd_username:
    entered_password = input (" please enter your password: ")
    if entered_password == password:
        os.system('clear') 
        print (" welcome " + user_name)
    else: 
        wants_hint_password = input (" would you like to see you hint for password? (yes or no)")
        if "yes" == wants_hint_password:
           print (hint_password)
        else:
            print ( colored ( " your a cupcake ", "green"))       
else:
    print ( colored(" your a fake user the computer will now be destroyed ", "black") ) 
