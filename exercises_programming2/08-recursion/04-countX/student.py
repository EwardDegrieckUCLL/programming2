def countX(text):
    if len(text) == 0:
        return 0
    
    last_char = text[-1]
    if last_char == 'x':
        return countX(text[:-1]) + 1 
    else:
        return countX(text[:-1])