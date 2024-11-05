def rle_encode(data):
    xs = iter(data)
    try:
        last_x = next(xs)
        count = 1
        for x in xs:
            if last_x == x:
                count += 1
        else:
            yield(last_x, count)
            last_x = x
            count = 1
        yield (last_x, count)
    except StopIteration:
        pass

def rle_decode(tuples):
    for x, count in tuples:
        for _ in range(count):
            yield x