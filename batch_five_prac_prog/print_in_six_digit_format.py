def prog02():

#Ask user to input a number between 0-1000
    while True:
        try:
            num = int(input("Enter a number between 0 to 1000: "))
            if 0 <= num <= 1000:
               break #Exit the loop if the input is valid
            else: #Else print the invalid number to enter new one
                print("Invalid input. Please enter a number between 0 to 1000.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 to 1000.")

#Format the number as 6 digit string with leading zeros
    formatted_num = "{:06d}".format(num)
    print(formatted_num)
prog02()