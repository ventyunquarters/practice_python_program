#Initialize an empty list to store the numbers
import numbers


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
    if not numbers:
        print("No valid numbers were entered.")
        return
#Initialize dictionary to store the count of each numbers
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    max_count = 0
    max_num = None
