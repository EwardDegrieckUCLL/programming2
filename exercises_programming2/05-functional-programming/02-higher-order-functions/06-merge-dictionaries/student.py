def merge_dictionaries(d1, d2, merge_function):
    result = {}

    for k1 in d1.keys():
        if k1 not in d2.keys():
                result[k1] = d1[k1]

    for k2 in d2.keys():    
        if k2 not in d1.keys():
                result[k2] = d2[k2]

    for k1, v1 in d1.items():
        for k2, v2 in d2.items():
            if k1 == k2:
                 result[k1] = merge_function(v1, v2)

    return result
