def is_prime(n):
    smaller = n-1
    while smaller > 1:
        if n % smaller == 0:
            return False
        smaller -= 1

    return n > 1