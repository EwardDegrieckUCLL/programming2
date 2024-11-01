def take_while(xs, condition):
    before = []
    for x in xs:
        if not condition(x):
            break
        before.append(x) 

    after = xs[len(before):]

    return (before, after)

    # hier zoek je eerste element met False value terwijl je de ene lijst opbouwt, in oplossing zoeken ze eerste index waarbij de False value verschijnt