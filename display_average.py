#Initialize an empty list to  store numbers
def prog05():
    numbers = []
#Loop indefinitely until an invaalid input is given
    while True:
        try:
#Get input and convert it to float.
            num = float(input("Enter a number (or non-numeric to stop): "))
            numbers.append(num)
        except ValueError:
            print("Invalid input. Ending program.")
            break
#Check if the list of numbers is not empty.
    if numbers:
#Calculate the average
        average = sum(numbers) / len(numbers)
        print("The average is: ", average)
    else:
        print("No valid numbers entered.")

prog05()

