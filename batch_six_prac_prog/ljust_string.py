def custom_ljust(input_string, length):

    if len(input_string) >= length:
        return input_string

    padding = " " * (length - len(input_string))
    return input_string + padding

#Get user input
user_statement = input("Enter your statement: ")
desired_length = int(input("Enter desired length: "))

#Ljust the string
left_justified_string = custom_ljust(user_statement, desired_length)

#display the result and used | as a marker
print("Left justified string: ", left_justified_string, "|")