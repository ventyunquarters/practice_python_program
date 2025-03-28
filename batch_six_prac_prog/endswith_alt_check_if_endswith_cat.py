#This will check if the string ends with the given suffix
def custom_endswith(input_string, suffix):
    if len(suffix) > len(input_string):
        return False
    return input_string[len(input_string) - len(suffix):] == suffix

#Ask for the user input
user_statement = input("Enter your statement that ends with cat: ")

#Check if the statement ends with "cat"
ends_with_cat = custom_endswith(user_statement, "cat")

#Display the result
print("Does the statement end with cat?",ends_with_cat)