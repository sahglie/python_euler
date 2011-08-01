#! /usr/bin/env python

import math

def primes_sieve(n):
    sieve = range(0, n+1)
    
    i = 2
    while i <= math.sqrt(len(sieve)):
        j = i+i
        while j < len(sieve):
            sieve[j] = 0;
            j += i
        else:
            i += 1
            while sieve[i] == 0:
                i += 1

    primes = set()
    for i in sieve:
        if i != 1 and i != 0:
            primes.add(i)

    return primes

def is_circular(num, primes):
    n = str(num)
    result = [True for i in range(0, len(n)) 
              if (int(n[i:len(n)] + n[0:i])) in primes]
    return len(result) == len(n)

def calc_circular_primes(n):
    primes = primes_sieve(n)
    circular_primes = []
    for prime in primes:
        if is_circular(prime, primes):
            circular_primes.append(prime)
    return circular_primes


    
if "__main__" == __name__:
    print len(calc_circular_primes(1000000))
    
