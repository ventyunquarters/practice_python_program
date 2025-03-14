#Initialize an empty list to store the numbers
def prog02():
    numbers = []
#Loop indefinitely until an invalid input is given
    while True:
        try:
            num = int(input("Enter a number: "))
            numbers.append(num)
        except ValueError:
            print("Invalid input. Ending program")
            break
#Check if the list of numbers is empty

#Initialize dictionary to store the count of each numbers

