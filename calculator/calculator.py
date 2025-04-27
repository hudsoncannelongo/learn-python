# Step 1: Ask the user for the first number and store it in a variable-
# Step 2: Ask the user for the operator (+, -, *, or /) and store it in a variable-
# Step 3: Ask the user for the second number and store it in a variable
# Step 4: Check which operation the user chose and perform it using if and elif statements
    # 4.1 If the operator is +, add the numbers and print the result
    # 4.2 If the operator is -, subtract the numbers and print the result
    # 4.3 If the operator is *, multiply the numbers and print the result
    # 4.4 If the operator is /, check for divide-by-zero and print the result
# Step 5: Print a message thanking the user for using the calculator

numberOne = input (" number one please ")
operator = input ( "+,-,* or / ")
numberTwo = input (" number two please ")

if operator == "+":
    print ( int(numberOne) + int ( numberTwo ))
elif operator == "-":
    print ( int( numberOne) - int ( numberTwo))
elif operator == "*":
    print ( int ( numberOne) * int (numberTwo))
elif operator == "/":
    print ( int ( numberOne) / int ( numberTwo))
else:
    print ( " maybe you didnt remeber what I said but you must enter a valide operator!!! ")
