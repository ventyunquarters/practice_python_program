#Ask the user input two numbers
def prog10():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
# Check if num1 is less than num2, print numbers from num1+1 to num2-1
    if num1 < num2:
        for num in range(num1 +1, num2):
            print(num)
# Check if num2 is less than num1, print numbers from num2+1 to num1-1
    elif num1 > num2:
        for num in range(num2 + 1, num1):

# If the numbers are equal, there are no numbers between them.
