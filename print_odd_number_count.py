#Initialize a variable to count odd numbers starting to 0
def prog08():
    odd_count = 0
#Prompt the user to enter a number
    for i in range(10):
        num = int(input(f"Enter a number {i +1}: "))
        if num % 2 != 0:
            odd_count += 1
#Print the number of odd numbers
    print("Number of odd numbers:", odd_count)

prog08()


