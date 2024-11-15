def remove_duplicates(xs):
    set_xs = set()
    result = []
    for x in xs:
        if x not in set_xs:
            result.append(x)
            set_xs.add(x)
    return result