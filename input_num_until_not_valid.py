#Initialize an empty list to store the numbers
def prog03():

    numbers = []
    while True:
        try:
#Get input and convert it to an integer
            num = int(input("Enter a number: "))
            if num in numbers:
                print("Duplicate")
            else:
                print("Unique")
                numbers.append(num)
#Handle invalid input
        except ValueError:
            print("Invalid input. Ending the program.")
            break
prog03()