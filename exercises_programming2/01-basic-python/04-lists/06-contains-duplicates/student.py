def contains_duplicates(xs):
    list_set = set()
    for x in xs:
        if x in list_set:
            return True
        list_set.add(x)

    return False