from re import fullmatch


def prog09():

#Ask the user to input their name with incorrect casing
    full_name = input("Enter your name with incorrect casting: ")
#Convert the title case and split into words
    words = full_name.title().split()
#Remove the spaces and join the words
    pascal_case_name = "".join(words)
#Print pascal case
    print(pascal_case_name)
prog09()