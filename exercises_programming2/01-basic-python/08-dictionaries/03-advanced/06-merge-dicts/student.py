def merge_dicts(dict1, dict2):
    result = {}
    for k,v in dict1.items():
        result[k] = v
    for a,b in dict2.items():
        result[a] = b
    return result