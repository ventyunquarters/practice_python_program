#Define function to remove the prefix without using the remove_prefix function
def alt_remove_prefix(input_string, prefix):

    if input_string.startswith(prefix):
        return input_string[len(prefix):]
    else:
        return input_string
#Ask the user to input their name with prefix(optional).
user_name = input("Enter your name (with optional prefix 'Mr. ' or 'Ms.'): ")
#Remove the prefix
cleaned_name = alt_remove_prefix(user_name, "Mr. ")
cleaned_name = alt_remove_prefix(cleaned_name, "Ms. ")
#Display the cleaned name
print("Your name without prefix: ", cleaned_name)