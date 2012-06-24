#!/usr/bin/env python

import math

def sieve_primes(n):
    primes = [1]*n
    for x in range(2, int(math.sqrt(n+1))+1):
        for y in range(2*x, n, x):
                primes[y] = 0
    return [i for (i,n) in enumerate(primes) if n and i > 1]

def prime_factors(n):
    factors = set()
    d = 2
    while n > 1:
        if n % d == 0:
            n /= d
            factors.add(d)
        else:
            d += 1
    return sorted(list(factors))

def prime_gen():
    D = {}
    p = 2
    while True:
        if p not in D:
            D[p * p] = [p]
            yield p
        else:
            for d in D[p]:
                D.setdefault(p + d, []).append(d)
            del D[p]
        p += 1

PANDIGITALS = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
def is_pandigital(n):
    """Determins if an integer contains all the digits 1-9 exactly once
    """
    if n < 123456789:
        return False
    
    used_digits = set([])
    while n:
        digit = n % 10
        if digit in used_digits:
            return False
        used_digits.add(digit)
        n /= 10
    return used_digits == PANDIGITALS


def make_n_pandigital(digits):
    pandigitals = set(range(1, digits+1))
    max = int("".join(map(str, list(pandigitals))))

    def is_pandigital(n):
        if n < max:
            return False

        used_digits = set([])
        while n:
            digit = n % 10
            if digit in used_digits:
                return False
            used_digits.add(digit)
            n /= 10
        return used_digits == pandigitals
    return is_pandigital
    

PRIME_CACHE = set()
def is_prime(n):
    if n in PRIME_CACHE: return True
    if n < 2: return False
    for i in xrange(2, int(n**.5+1)):
        if n % i == 0: return False
    PRIME_CACHE.add(n)
    return True
