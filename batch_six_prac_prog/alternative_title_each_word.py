def alternative_title(input_string):

    if not input_string:
        return ""

    result = ""
    capitalize_next = True #Marker to capitalize the next character"

    for char in input_string:
        if char.isalppha():
            if capitalize_next:
                if 'a' <= char <= 'z':
                    result += chr(ord(char) - 32) #capitalize
                else:
                    result += char
                capitalize_next = False
            else:
                if 'A' <= char <= 'Z':
                    result += chr(ord(char) + 32) #Lowercase
                else:
                    result += char
