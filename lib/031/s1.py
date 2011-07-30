#! /usr/bin/env python

import math

"""
The number, 197, is called a circular prime because all rotations 
of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""


def prime_gen(limit):
    num = 2
    while num < limit:
        if is_prime(num):
            yield num
            num += 1
        else:
            num += 1

primes_cache = set([2])
def is_prime(num, cache=primes_cache):
    if num in primes_cache:
        return True

    if num == 0 or num == 1:
        return False
    else:
        for n in range(2, int(math.sqrt(num))+1):
            if num % n == 0:
                return False
        if num not in primes_cache:
            cache.add(num)
        return True

def is_circular_prime(num):
    if not is_prime(num):
        return False

    primes = []
    n = str(num)
    result = [True for i in range(0, len(n)) 
              if is_prime(int(n[i:len(n)] + n[0:i]))]
    return len(result) == len(n)

if __name__ == "__main__":
    print len([n for n in prime_gen(1000000)
               if is_circular_prime(n)])
