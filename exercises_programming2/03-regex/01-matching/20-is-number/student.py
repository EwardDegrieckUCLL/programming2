import re

def is_number(string):
    return re.fullmatch(r'\d+(\.\d+)?', string)

    # instead of using \ before character, you could also put that character in brackets. This avoids invalid escape sequence error
    # \. --> [.]
    # BUT if you use raw string, it is again ok to \.