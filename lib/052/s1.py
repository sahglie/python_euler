#!/usr/bin/env python

"""The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a
prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""

import os, sys
package_root = os.path.abspath(os.path.curdir).split("/")
package_root.pop()
sys.path.insert(0, "/".join(package_root))

from utils import is_prime, primes_sieve

def find_max(primes):
    sum = 0;
    for x in xrange(0, len(primes)):
        sum += primes[x]
        if sum > primes[-1]: break
    return x

def build_sums(primes):
    start = find_max(primes)
    sums = {}
    sums[start] = sum(primes[0:start])

    while start > 1:
        start -= 1
        sums[start] = sums[start+1] - primes[start]
    return sums
        
def calc_curr_sum(first, last, sums):
    if first > 0:
        return sums[last] - sums[first]
    else:
        return sums[last]
            
def main():
    MAX = 1000000
    
    best = (0, 0)
    primes = primes_sieve(MAX)
    sums = build_sums(primes)
    for first in xrange(0, len(sums)):
        last = len(sums)
        while last-first > best[1]:
            curr_sum = calc_curr_sum(first, last, sums)
            if is_prime(curr_sum):
                best = (curr_sum, last-first)
                break
            last -= 1
    print best

    
if __name__ == "__main__":
    main()
            
