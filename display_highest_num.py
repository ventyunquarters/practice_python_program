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


