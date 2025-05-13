
from termcolor import colored
import time
import credentials
import random
import os 


def startNumberGame():
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

def start_Password ():
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
        startNumberGame()
    else: 
        print ( colored ("you are a failure", "blue" ) )

start_Password()