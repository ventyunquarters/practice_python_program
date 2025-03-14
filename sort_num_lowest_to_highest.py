#Initialize an empty list to store numbers
import numbers
def prog05():
    numbers = []
#Loop indefinitely until an invalid input is given
    while True:
        try:
            num = int(input("Enter a number: "))
            numbers.append(num)
        except ValueError:
            print("Invalid input. Ending program.")
            break
#Check if the list of numbers is not empty
    if numbers:
        numbers.sort()
        print("Numbers from lowest to highest:", numbers)
    else:
        print("No valid numbers were entered.")

prog05()

