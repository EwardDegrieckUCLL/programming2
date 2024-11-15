import re

def is_valid_password(string):
    
    valid = [
        r'\d',
        r'[a-z]',
        r'[A-Z]',
        r'[-+*/.@]'
    ]

    invalid = [
        r'(.)\1{2}',
        r'(.)(.*\1){3}'
    ]

    for regex in valid:
        if not re.search(regex, string):
            return False
        
    for regex in invalid:
        if re.search(regex, string):
            return False

    return len(string) >= 12