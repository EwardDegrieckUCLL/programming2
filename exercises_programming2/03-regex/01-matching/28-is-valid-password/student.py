import re

def is_valid_password(string):
    pos_regex = [
        r'.{12,}',
        r'[0-9]',
        r'[a-z]',
        r'[A-Z]',
        r'[-+/.*@]',
    ]

    neg_regex= [
        r'(.)\1{2}',
        r'(.)(.*\1){3}'
    ]

    for regex in pos_regex:
        if not re.search(regex, string):
            return False
        
    for regex in neg_regex:
        if re.search(regex, string):
            return False
        
    return True
