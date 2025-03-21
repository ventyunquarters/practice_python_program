def prog02():

#Ask user to input a number between 0-1000
    while True:
        try:
            num = int(input('Enter a number between 0 to 1000: '))
            if 0 <= num <= 1000:
                break
            else:

#Exit the loop if the input is valid

#Else print the invalid number to enter new one

#Formatt he number as 6 digit string with leading zeros
