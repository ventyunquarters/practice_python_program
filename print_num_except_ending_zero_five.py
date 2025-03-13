# Define program and loop through numbers from 0 to 100
def prog09():
    for num in range (101):
#Check if the number does NOT end with 0 and 5
        if num % 10 != 0 and num % 10 != 5:
            print(num)

prog09()

