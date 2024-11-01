def rotate(xs, n):
    part1 = xs[:n]
    part2 = xs[n:]
    return part2 + part1
