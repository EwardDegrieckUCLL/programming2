def sum_numbers(number):
    number = abs(number)

    if number < 10:
        return number

    last_number = number % 10
    rest = number // 10
    
    return last_number + sum_numbers(rest)