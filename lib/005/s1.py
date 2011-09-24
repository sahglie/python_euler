#!/opt/local/bin/python


"""2520 is the smallest number that can be divided by each of
the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by
all of the numbers from 1 to 20?
"""

def prime_gen():
    D = {}
    q = 2
    while True:
        if q not in D:
            D[q * q] = [q]
            yield q
        else:
            for p in D[q]:
                D.setdefault(q + p, []).append(p)
            del D[q]
        q += 1


if "__main__" == __name__:
    prime_factors = {}
    for i in range(2, 21):
        factors = {}
        n = i
        for prime in prime_gen():
            if prime > i:
                break
            elif prime == i:
                prime_factors[prime] = 1
                break
            while n != 1:
                if n % prime == 0:
                    factors[prime] = factors.get(prime, 0) + 1
                    n /= prime
                else:
                    break
            if prime_factors.get(prime):
                prime_factors[prime] = max(factors.get(prime),
                                           prime_factors[prime])
                
    total = 1
    for p in prime_factors.keys():
        total *= p**prime_factors[p]
    print total
