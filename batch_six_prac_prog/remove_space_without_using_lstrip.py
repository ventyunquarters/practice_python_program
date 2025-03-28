#Define the alternative lstrip use args to process the string and returns with leading whitespace removed
def custom_lstrip(input_string):
    i = 0
    while i < len(input_string) and input_string[i].isspace():
        i += 1
    return input_string[i:]
# Ask the user to input their name
user_name = input("Enter your name: ")
# Remove the leading whitespace
cleaned_name = custom_lstrip(user_name)
# Display the cleaned name
print("Your name without leading space: ", cleaned_name)
