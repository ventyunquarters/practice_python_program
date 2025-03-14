#Initialize an empty list to store numbers
def prog01():
    numbers = []
#Loop 10 times to get 10 numbers from user.
    for i in range(10):
#Get input and convert it to integer
        num = int(input(f"Enter a number {i+1}: "))
        numbers.append(num)
#Initialize an empty list
    unique_numbers = []
#Iterate through the list of numbers
    for num in numbers:
#Check if the number appears only once in the list.
        if numbers.count(num) == 1:
            unique_numbers.append(num)
#Print the list of unique numbers.
    print("Number of unique numbers: ", (unique_numbers))

prog01()