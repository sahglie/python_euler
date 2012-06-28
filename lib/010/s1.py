#! /usr/bin/env python

import math


def primes_sieve(n):
    if n == 2:
        return [2]
    elif n < 2:
        return []

    sieve = list(range(0, n))
    l = len(sieve)
    
    i = 2
    while i < math.sqrt(l):
        j = i+i
        while j < l:
            sieve[j] = 0
            j += i
        else:
            i += 1
            while sieve[i] == 0:
                i += 1

    return [i for i in sieve if i > 1]

print(sum(primes_sieve(2000000)))
