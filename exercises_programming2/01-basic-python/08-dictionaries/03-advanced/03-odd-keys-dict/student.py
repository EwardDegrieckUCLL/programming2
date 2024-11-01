def odd_keys_dict(dictionary):
    result = {}
    for key in dictionary.keys():
        if key % 2 != 0:
            result[key] = dictionary[key]
    return result