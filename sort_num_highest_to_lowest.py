def prog04():
#Add empty list to store the numbers.
    numbers = []
#Add loop until an invalid input is given
    while True:
        try:
#Get input and convert it to an integer.
            num = int(input("Enter a number: "))
            numbers.append(num)
        except ValueError:
            print("Invalid input. Ending program.")
            break
#Check the list of number is not empty.
    if numbers:
#Sort numbers in descending order using function
        numbers.sort(reverse=True)
        print("Numbers sorted in descending order:", numbers )
    else:
        print("No valid numbers found.")
prog04()