def includes(xs, ys):
    set_xs = set(xs)
    set_ys = set(ys)
    return set_ys - set_xs == set()
