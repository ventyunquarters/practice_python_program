def custom_ljust(input_string, length):

    if len(input_string) >= length:
        return input_string

    padding = " " * (length - len(input_string))
    return input_string + padding
