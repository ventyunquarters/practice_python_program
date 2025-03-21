def prog06():

#Ask user to input their name with incorrect casing
    full=name = input("Enter your full name with incorrect casing: ")
    reversed_case_name = " "
#Iterate through each character in the input string
    for char in full_name:
#Check if the character is lowercase
        if char.islower():
#Convert to uppercase and append.
            reversed_case_name += char.upper()
#Check if the character is uppercase.
        elif char.isupper():
            reversed_case_name += char.lower()
#Convert to lowercase and append.

#Print reversed case name

