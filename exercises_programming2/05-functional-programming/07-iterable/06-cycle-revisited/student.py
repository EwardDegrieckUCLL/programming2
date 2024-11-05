def cycle(string):
    index = 0
    while True:
        yield string[index % len(string)]
        index += 1