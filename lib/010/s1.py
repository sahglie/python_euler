#! /usr/bin/env python

import math


def primes_sieve(n):
    if n == 2:
        return [2]
    elif n < 2:
        return []

    sieve = range(0, n+1)
    
    i = 2
    while i < math.sqrt(len(sieve)):
        j = i+i
        l = len(sieve)
        while j < l:
            sieve[j] = 0
            j += i
        else:
            i += 1
            while sieve[i] == 0:
                i += 1

    return [i for i in sieve if i != 0 and i != 1]


if "__main__" == __name__:
    print sum(primes_sieve(2000000))
