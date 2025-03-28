#Define the function isupper using args
def custom_isupper(input_string):

    for char in input_string:
        if 'a' <= char <= 'z':
            return False
        elif 'A' <= char <= 'Z':
            continue
        else:
            if char.isalpha():
                return False
    return True
