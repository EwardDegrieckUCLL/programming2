def card_value(string):
    dict = {'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 1}
    for k, v in dict.items():
        if k == string:
            return v
    
    return int(string)