#Initialize variable to count even numbers. Start at 0
def prog07():
    even_count = 0
#Loop 10 times to get 10 numbers from the user.
    for i in range(10):
        num = int(input(f"Enter a number {i + 1}: "))
#Check if the number is even
    if num % 2 == 0:
        even_count += 1
#Print the total count of even numbers,