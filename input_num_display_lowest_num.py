#Initialize an empty list to store the num
def prog04():
    numbers = []
#Loop indefinitely until an invalid input is given
    while True:
        try:
            num = int(input("Enter a number: "))
            numbers.append(num)
        except ValueError:
            print("Invalid input. Ending program.")
            break
#Check if the list of numbers is not empty.