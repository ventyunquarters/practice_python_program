#Ask the user to input two numbers
def prog04():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
#Check if the second number is zero
    if num2 == 0:
        print("Cannot divide by zero.")
#Calculate the integer quotient using floor division
    else:
        quotient = num1 // num2
# Print the integer quotient
        print("The quotient is: ", quotient)

prog04()
