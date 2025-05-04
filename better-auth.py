#  1. Make a SEPERATE FILE called credentials.py-

#  2. In that NEW file, create a variable called username and a variable called password -

#  3. Assign the username and password variables to the values you want -

#  4. Import the username and password variables from the credentials.py file into the THIS file (from credentials import username, password)-

#  5. Ask the user to enter a username

# 6. Ask the user to enter a password -

# 7. Use a while loop to keep asking if the username OR password is wrong: - 
    # 8. Tell the user "Incorrect, try again" -
    # 9. Ask again for the username -
    # 10. Ask again for the password -

# 11. When the username AND password are correct, say "Access granted!"

# 12. BE CREATIVE!  Add some extra features to this code.  For example, you could add a limit to how many times the user can try to enter the username and password, maybe add a password hint, etc.
from termcolor import colored

import time


import credentials

import random
import os 
os.system ("clear")
enterd_username = input ("whats the name??: ")
enterd_password = input("please enter your password: ")

tries = 0
limit_tries = 3

while (enterd_username != credentials.username or enterd_password != credentials.password ) and tries <= limit_tries:
    os.system("clear")
    print ("incorrect attempt!  you have " + str (limit_tries - tries ) + " tries left ")
    
    wantspassword_hint = input ("would you like to see you password hint? YES or NO: ")
    
    if wantspassword_hint == "yes":
        print (credentials.password_hint)
        time.sleep(3)
    os.system ("clear")   
    tries += 1
    enterd_username = input (  colored  ("please try the username again: ", "red") ) 
    enterd_password = input ( colored (" please enter the right password ", "green") )

if enterd_password == credentials.password and enterd_username == credentials.username:
    os.system ("clear")
    secret_number = random.randint(1,10)

    guess =  int ( input (" what's your guess for the number game? "))

    tries = 0
    limit_of_tries = 5
    while guess != secret_number and tries != limit_of_tries:   
        
        tries += 1

        if guess > secret_number: 
            print (' too high go lower now!!! ')
        
        elif guess < secret_number:
            print (' too low go higher bud!!!')

        guess = int ( input(' guess again you bud!!!  you have ' + str(  limit_of_tries - tries ) + " more guesses left: " ))



    if tries == limit_of_tries:
        print ('ugh you lost boring bum! ')
    elif guess == secret_number:
        print (   colored (" you're right ", "green")   )

else: 
    print ( colored ("you are a failure", "blue" ) )