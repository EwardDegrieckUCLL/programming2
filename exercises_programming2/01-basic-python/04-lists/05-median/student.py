def median(ns):
    sorted_ns = sorted(ns.copy())
    if len(ns) % 2 != 0:
        # list has odd amount of elements
        index = len(ns)//2
        return sorted_ns[index]
    else:
        # even amount of elements
        index2 = len(ns)//2
        index1 = index2-1
        return (sorted_ns[index1] + sorted_ns[index2]) / 2
