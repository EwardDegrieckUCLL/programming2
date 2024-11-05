def fizzbuzz():
    index = 0   
    # because first item is already 1 (otherwise start with -1)
    while True:
        index += 1
        if index % 15 == 0:
            yield 'fizzbuzz'
        elif index % 5 == 0:
            yield 'buzz'
        elif index % 3 == 0:
            yield 'fizz'
        else:
            yield str(index)
