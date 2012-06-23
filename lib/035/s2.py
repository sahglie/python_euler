#! /usr/bin/env python

import math

def primes_sieve2(n): 
    if n == 2:
        return [2]
    elif n < 2:
        return []

    s = range(3, n+1, 2)
    mroot = n ** 0.5
    half = (n+1)/2-1
    i = 0
    m = 3
    while m <= mroot:
        if s[i]:
            j = (m*m-3)/2
            s[j] = 0
            while j < half:
                s[j] = 0
                j += m
        i = i + 1
        m = 2 * i + 3
    return [2] + [x for x in s if x]
    
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

def is_circular(num, primes):
    n = str(num)
    result = [1 for i in range(0, len(n)) 
              if (int(n[i:len(n)] + n[0:i])) in primes]
    return len(result) == len(n)

def calc_circular_primes(n):
    primes = primes_sieve(n)
    primes_set = set(primes)
    circular_primes = []
    for prime in primes:
        if is_circular(prime, primes_set):
            circular_primes.append(prime)
    return circular_primes


    
if "__main__" == __name__:
    print len(calc_circular_primes(1000000))
    
