import re

def is_number(string):
    return re.fullmatch('[0-9]+([.][0-9]+)?', string)

    # instead of using \ before character, you could also put that character in brackets. This avoids invalid escape sequence error
    # \. --> [.]