def prog04():
#Add empty list to store the numbers.
    numbers = []
#Add loop until an invalid input is given
    while True:
        try:
            num = int(input("Enter a number: "))
            numbers.append(num)
        except ValueError:
            print("Invalid input. Ending program.")
        break
#Get input and convert it to an integer.

#Check the list of number is not empty.

#Sort numbers in descending order using function

