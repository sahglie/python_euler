#!/usr/bin/env python

"""The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms are
prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

import os, sys
package_root = os.path.abspath(os.path.curdir).split("/")
package_root.pop()
sys.path.insert(0, "/".join(package_root))

from utils import is_prime

from itertools import permutations, combinations


if __name__ == "__main__":
    solutions = {}
    primes = [p for p in xrange(1000, 10000) if is_prime(p)]
    
    for prime in primes:
        candidates = []
        for p in permutations(str(prime)):
            x = int("".join(p)) 
            if is_prime(x): candidates.append(x)
            
        for c in combinations(set(candidates), 3):
            if c[0] == prime and c[2] - c[1] == c[1] - c[0]:
                solutions[prime] = "%s%s%s" % (c[0], c[1], c[2])
                
    print solutions
            
