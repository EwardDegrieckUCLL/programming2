def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2,n))

def primes():
    n = 1
    while True:
        n += 1
        if is_prime(n):
            yield n