#Define the function isupper using args
def custom_isupper(input_string):

    for char in input_string:
        if 'a' <= char <= 'z':
            return False
        elif 'A' <= char <= 'Z':
            continue
        else:
            if char.isalpha():
                return False
    return True
#Ask user for a statement
user_statement = input("Enter your statement: ")

#Check if the statement is all uppercase
is_uppercasse = custom_isupper(user_statement)

# Display the result
print("Is the statement all uppercase?",is_uppercasse)