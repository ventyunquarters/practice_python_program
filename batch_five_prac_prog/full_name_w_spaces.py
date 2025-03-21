def prog01():

#Ask the user to input their full name with leading spaces
    full_name = input("Enter your full name with leading spaces: ")
#Use an lstrip to remove the leading spaces
    trimmed_name = full_name.strip()
#Print trimmed name
    print(trimmed_name)
prog01()