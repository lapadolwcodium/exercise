def sieve(limit):
    re_primes = set()
    primes = []
    if limit > 1:
        primes.append(2)

    for counting in range(3, limit + 1, 2):
        if counting not in re_primes:
            primes.append(counting)
            re_primes.update(range(counting ** 2, limit, counting))
            # print ("re_prime", range(counting ** 2, limit, counting))

    # print ("limit", limit, primes)
    return primes
