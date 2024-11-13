def reverse_from_left(text):
    if len(text) == 0:
        return text
    
    return reverse_from_left(text[1:]) + text[0]

def reverse_from_right(text):
    if len(text) == 0:
        return text
    
    return text[-1] + reverse_from_right(text[:-1])