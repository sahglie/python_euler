#!/opt/local/bin/python


"""2520 is the smallest number that can be divided by each of
the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by
all of the numbers from 1 to 20?
"""

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19]

if "__main__" == __name__:
    prime_factors = {}
    for n in xrange(2, 21):
        factors = {}
        i = n
        for prime in PRIMES:
            if prime > n:
                break
            elif prime == n:
                prime_factors[prime] = 1
                break
            while i > 1:
                if i % prime:
                    break
                i /= prime
                factors[prime] = factors.get(prime, 0)
                factors[prime] += 1

        for f in factors.keys():
            if prime_factors.get(f, 0) < factors[f]:
                prime_factors[f] = factors[f]

    total = 1
    for i in prime_factors.keys():
        total *= (i**prime_factors[i])

    print total
