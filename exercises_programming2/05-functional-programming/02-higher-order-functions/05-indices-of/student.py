def indices_of(xs, condition):
    return [
        index for index, x in enumerate(xs)
        if condition(x)
    ]