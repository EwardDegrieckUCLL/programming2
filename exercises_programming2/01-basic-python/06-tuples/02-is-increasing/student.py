def is_increasing(ns):
    ms = ns[1:]
    paired_with_successor = list(zip(ns, ms))
    for x, y in paired_with_successor:
        if x > y:
            return False
    return True
