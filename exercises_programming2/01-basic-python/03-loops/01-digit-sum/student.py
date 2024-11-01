def last_digit(n):
    return n % 10

def remove_last_digit(n):
    return n // 10

def digit_sum(n):
    total = 0
    while n > 0:
        last = last_digit(n)
        total += last
        n = remove_last_digit(n)
    
    return total