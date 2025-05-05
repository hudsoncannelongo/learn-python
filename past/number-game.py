# 1. First, we need to get random numbers, so: import random

# 2. Make a variable that picks a random number between 1 and 10: random.randint(1, 10)

# 3. Ask the user to guess a number using input()
# Turn it into a number with int()

# 4. Use a while loop to loop every time the guess is NOT equal to the secret number

    # 5. If the guess is too high, print "Too high!"

    # 6. else If the guess is too low, print "Too low!"

    # 7. Ask again and get a new guess

# 8. When the guess is right, print "You got it!" in green




from termcolor import colored

import os
import random 

os.system ("clear")

secret_number = random.randint(1,10)

guess =  int ( input (" whats you guess for the number game? "))

tries = 0
limit_of_tries = 5
while guess != secret_number and tries != limit_of_tries:   
    
    tries += 1

    if guess > secret_number: 
        print (' to high go lower now!!! ')
    
    elif guess < secret_number:
        print (' too low go higher bud!!!')

    guess = int ( input(' guess again you bud!!!  you have ' + str(  limit_of_tries - tries ) + " :more guesses left: " ))



if tries == limit_of_tries:
    print ('ugh you lost boring bum! ')
elif guess == secret_number:
    print (   colored (" your right ", "green")   )










