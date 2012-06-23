#! /usr/bin/env python


"""The number 3797 has an interesting property. Being prime
   itself, it is possible to continuously remove digits from
   left to right, and remain prime at each stage:
   
   3797, 797, 97, and 7.

   Similarly we can work from right to left:

   3797, 379, 37, and 3.

   Find the sum of the only eleven primes that are both truncatable
   from left to right and right to left.
   """

def truncated_subsets(prime):
    if len(prime) == 1: return [prime]
    subsets = []
    for i in range(1, len(prime)):
        subsets.append(prime[i:len(prime)])
        subsets.append(prime[0:len(prime)-i])
    return subsets

def is_truncatable_prime(prime, primes):
    subsets = truncated_subsets(prime)
    truncatable_primes = [i for i in subsets if i in primes]
    return len(truncatable_primes) == len(subsets)
        
def prime_gen():
    """ Generate an infinite sequence of prime numbers.
    """
    import pdb
    pdb.set_trace()
    
    D = {}  
    q = 2  
    while True:
        if q not in D:
            yield q        
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1
        
def truncatable_primes_upto(n):
    primes = set()
    truncatable_primes = []
    for prime in prime_gen():
        primes.add(str(prime))
        if len(str(prime)) > 1 and \
               is_truncatable_prime(str(prime), primes):
            truncatable_primes.append(prime)
        if len(truncatable_primes) == n:
            return truncatable_primes

    
if "__main__" == __name__:
    g = prime_gen()

    for i in range(1, 10):
        print g.next()
    # print sum(truncatable_primes_upto(11))
