import re 

def remove_repeated_words(string):
    return re.sub(r'(\b[a-zA-Z]+\b)(\s\1)+', r'\1' , string)