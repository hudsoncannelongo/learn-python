
import os
import time 
import termcolor


def startBank ():
    os.system("clear")

    balance = int (input ( termcolor.colored ("How much cash are we tossin' into the digital piggy bank today? 🐷✨: ", "blue") ) )

    os.system ("clear")

    print ("Welcome to huddies Venmo ") 

    time.sleep(3)

    os.system("clear")

    while True :
        print ("Type 'd for Deposit your money")
        print ("Tpye 'v' to veiw your money that you added ")
        print ("Type 'w' for withdraw money ")
        print ("Tpe 'r' to recheck your money ")
        print ("type 'e' to exit")
        choice = input( termcolor.colored ("What's your choice: ", "blue") )
        
        os.system("clear")

        if choice == "v" : 
            print ("you have this much money " + str (balance ))
        elif choice == "w" : 
            withdraw_amount = int ( input( termcolor.colored("how much money are we sending away?: ", "blue") ) )
            balance -= withdraw_amount
            print (" this is how much you have " + str (balance))
        elif choice == "d" : 
            deposit_amount = int (input( termcolor.colored("how much money are we adding: ", "blue")))
            balance += deposit_amount 
            print ("deposit success " + str (balance))
        elif choice == "r":
            print ("checking your money... ")
            time.sleep (3) 
            os.system ("clear")
            balance = 0
            print ( "haha you'v been robed")
        elif choice == "e":
            break

        else:
            print ("you must type the choices above!!")
        
        time.sleep(3)
        os.system("clear")



    os.system ("clear")
    print ("good buy brian")
    time.sleep (3)
    os.system ("clear")


os.system("clear")
password = "123"
entered_password = input("what's the password")
if password == entered_password:
    startBank()