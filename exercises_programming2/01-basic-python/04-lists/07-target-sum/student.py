def target_sum(ns, target):
    return any(
        x + y == target
        for x in ns
        for y in ns
    )

# remade exercise after learning about comprehensions