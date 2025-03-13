#Ask user to input two numbers
def prog05():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
#Print cannot be divide by zero if num2 is equal to 0
    if num2 == 0:
        print("Cannot divide by zero")
#Print the quotient
    else:
        quotient = num1 // num2
        print(quotient)
#Call the function
prog05()