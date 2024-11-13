def findMaximum(list):
    if not list:
        raise IndexError()
    
    first_element = list[0]
    rest = list[1:]

    # base case
    if len(list) == 1:
        return first_element
    
    # recursion
    if first_element >= findMaximum(rest):
        return first_element
    else:
        return findMaximum(rest)