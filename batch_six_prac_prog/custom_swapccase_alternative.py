def alternative_swapcase(input_string):

    result = ""
    for char in input_string:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32) #Converts lowercase to upper
        elif 'A' <= char <= 'Z':
            result += chr(ord(char) + 32) #Converts uppercase to lowercase
        else:
            result += char
    return result

#Ask for user input
user_string = input("Enter your statement: ")

#Swap the casing
swapped_string = alternative_swapcase(user_string)

#Display the result
print("Swapped casing:", swapped_string)
