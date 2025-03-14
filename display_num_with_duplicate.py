import numbers


def prog01():

#Initialize an empty list to store the numbers.
    numbers = []
#Loop 10 times to get 10 numbers from the user.
    for i in range(10):
        num = int(input(f"Enter a number {i+1}: "))
#Add number to the list.
        numbers.append(num)
#Initialize an empty list and set to track seen numbers.
    duplicates = []
    seen = set()
#Iterate through the list of numbers.
