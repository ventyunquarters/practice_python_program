def prog10():

#Ask user to print full name with incorrect casing
    full_name = input("Enter your name with incorrect casting: ")
#Use the character to see if the character is alphanumeric it would keep it otherwise it would be replaced with a space
    words = "".join(c if c.isalnum() else " " for c in full_name).lower().split()
#Join the words and add the _ to replace space
    snake_case_name = "_".join(words)
#Print snake case
    print(snake_case_name)
prog10()