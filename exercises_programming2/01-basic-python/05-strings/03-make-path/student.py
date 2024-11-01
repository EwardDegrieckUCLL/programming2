def make_path(parts):
    if len(parts) == 0:
        return ''
    string = parts[0]
    for part in parts[1:]:
        string += '/' 
        string += part
    return string
