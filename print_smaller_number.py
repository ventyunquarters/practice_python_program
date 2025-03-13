#Ask user to input two numbers
def prog01():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
#Add if condition to check if num1 is less than num2
    if num1 < num2:
        print("The smallest number is: ", num1)
#Otherwise print num 2 if they are smaller or equal
    else:
        print("The smallest number is: ", num2)
#Call the function
prog01()
