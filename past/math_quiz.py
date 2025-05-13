import random
import os
import termcolor
import time 
os.system("clear")
question_count = 0 
total_queston = 5
score = 0
print ("welcome to huddies math game, also Type exit if you want to leave the page ")
time.sleep (3)
os.system("clear")

while True : 
    num1 = random.randint (1,100)
    num2 = random.randint (1,100)
    correct_answer = num1 + num2 
    enterd_attempt =  input (f"whats the answer to {num1} + {num2}: ")
    
    if enterd_attempt == "exit" :
        break 
    elif enterd_attempt.isdigit() and int(enterd_attempt) == correct_answer:
        score += 1        
        print (f"correct your score is {score}" )
    elif enterd_attempt.isdigit() and int (enterd_attempt) != correct_answer:
        
        print ( f"wrong its {correct_answer} your score is still {score}")
    else:
        print ("you must answer the question!!! ")
    time.sleep (3)
    os.system ("clear")
    question_count += 1
    if question_count == total_queston:
        break
print (f"good bye your score is {score}!!!")
