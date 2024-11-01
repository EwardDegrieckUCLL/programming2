def cakes(eggs, butter, flour):
    eggs_limit = eggs // 5
    butter_limit = butter // 250
    flour_limit = flour // 250
    return min(eggs_limit, butter_limit, flour_limit)