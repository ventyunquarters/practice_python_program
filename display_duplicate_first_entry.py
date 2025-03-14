#Initialize an empty list to store the numbers
def prog02():
    numbers = []
#Loop 10 times to get 10 numbers from the user
    for i in range(10):
        num = int(input(F"Enter number {i + 1}: "))
        numbers.append(num)
#Initialize an empty lise to track numbers already printed
    seen_numbers = []
    for num in numbers:

#Check if the number has not been printed yet.
        if num not in seen_numbers:
            print(num)
            seen_numbers.append(num)
prog02()
