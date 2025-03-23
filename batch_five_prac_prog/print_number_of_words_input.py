def prog07():
#Ask user to input a complete statement
    statement = input("Enter your statement: ")
#Using function split we are going to make it into list of words
    words = statement.split()
#Use lens function to get the number of words
    word_count = len(words)
#print the word count
    print(word_count)
prog07()
