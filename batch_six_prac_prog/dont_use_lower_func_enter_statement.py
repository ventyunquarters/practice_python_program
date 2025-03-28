#Define custom lower using string to convert all characters in a string to lowercase
def custom_lower(input_string):

#Convert the result to lowercase
    result  = ""
    for char in input_string:
        if 'A' <= char <= 'Z':
            #Use ASCII values
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

#Ask the user for input
user_statement = input("Enter your statement: ")

#Convert to lowercase
lower_statement = custom_lower(user_statement)

#Display the result
print("Lowercase statement:", lower_statement)