import os
import time

os.system("clear")

print("Hello, welcome to the bank application!")

time.sleep(3)

os.system("clear")

money = int(input("How much money do you have to start?: "))

while True:
    print("Type 'v' for view yo money")
    print("Type 'w' for withdraw money")
    print("Type 'd' for deposit money")
    print("Type 'r' for allowing me to ROB your money")
    print("Type 'e' for EXIT")

    decision = input("Make your choice: ")

    os.system('clear')

    if decision == "v":
        print("You have " + str(money) + " dollars left in your account")

    elif decision == "w":
        withdraw_amount = int( input("How much do you want to withdraw: ") )
        if withdraw_amount > money:
            print("Your too poor")
        else: 
            money -= withdraw_amount
            print("Withdraw success!")

    elif decision == "d":
        deposit_amount = int( input("How much would you like to deposit?: ") )
        money += deposit_amount
        print("Transfer/Deposit Success!")

    elif decision == 'r':
        money = 0
        print("HAHAHAHA! Robbing complete!")

    elif decision == "e":
        break

    else:
        print("¡No lo entraste correctamente!")

    time.sleep(3)
    os.system("clear")
    

os.system("clear")
print("GOODBYE SEE YA LATER")