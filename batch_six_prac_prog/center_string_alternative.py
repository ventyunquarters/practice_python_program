def custom_center(input_string, length):

    if len(input_string) >= length:
        return input_string #NO padding needed

    padding_length = length - len(input_string)
    left_padding = " " * (padding_length // 2)
    right_padding = " " * (padding_length - len(left_padding))

    return left_padding + input_string + right_padding
