def alternative_capitalize(input_string):
    if not input_string:
        return ""

    first_char = input_string[0]
    res_of_string = input_string[1:]

    if 'a' <= first_char <= 'z':
        capitalized_first = chr(ord(first_char) -32)
    else:
        capitalized_first = first_char

    lowercase_others = ""
    for char in rest_of_string:
        if 'A' <= char <= 'Z':
            lowercase_others += chr(ord(char) + 32)
        else:
            lowercase_others += char

    return capitalized_first + lowercase_others
