#Initialize an empty list to store the numbers
from unittest import result


def prog06():
    numbers = []
#Loop 10 times to get 10 numbers from the user.
    for i in range(10):
#Get input and convert it to an integer.
        num = int(input(f"Enter number{i + 1}: "))
        numbers.append(num) #Add number to the list
#Initialize result with the first number on the list
    result = numbers[0]
    for i in range (1, 10):
        result -= numbers[i]
#Print final result
    print("Result:", result)

prog06()
