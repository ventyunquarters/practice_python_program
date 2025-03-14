def prog03():

#Add an empty list to store the numbers
    numbers = []
    while True:
        try:
#Get an input and convert it to integer
            num = int(input("Enter a number: "))
            numbers.append(num)
        except ValueError:
            print("Invalid input. Ending program.")
            break
#Check if the list of numbers is not empty
    if numbers:
        highest_number = max(numbers)
        print("The highest number is: ", highest_number)
    else:
        print("No valid numbers found.")
prog03()


