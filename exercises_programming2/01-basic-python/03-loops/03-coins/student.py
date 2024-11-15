def coins(one, two, five, goal):
    return any(
        1*x + 2*y + 5*z == goal
        for x in range(one+1)
        for y in range(two+1)
        for z in range(five+1)
    )

# remade this exercise after completing chapter about comprehensions