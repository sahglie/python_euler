#!/usr/bin/env python

import os, sys
package_root = os.path.abspath(os.path.curdir).split("/")
package_root.pop()
sys.path.insert(0, "/".join(package_root))

from utils import is_prime


if __name__ == "__main__":
    primes, total = 0, 1
    ratio = 1.0
    for i in xrange(3, 1000000, 2):
        total += 4
        sqr = i**2
        corners = (sqr, sqr-(i-1), sqr-2*(i-1), sqr-3*(i-1))
        primes += len([n for n in corners if is_prime(n)])
        ratio = float(primes)/float(total)
        if ratio < 0.1:
            break
    print i
        
