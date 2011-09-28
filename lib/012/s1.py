#!/opt/local/bin/python

"""The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be:

1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.

The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred
divisors?
"""

def prime_gen():
    D = {}
    p = 2
    while True:
        if p not in D:
            D[p * p] = [p]
            yield p
        else:
            for d in D[p]:
                D.setdefault(p + d, []).append(d)
            del D[p]
        p += 1


def triangle_num_gen():
    n = 1
    while True:
        yield (n*(n+1))/2
        n += 1


def num_divisors(tri):
    factors = {}
    n = tri
    for prime in prime_gen():
        if n == prime:
            factors[prime] = 1
            break
        while (n % prime == 0) and n != 1:
            n /= prime
            factors[prime] = factors.get(prime, 0) + 1
        if n == 1:
            break
    num_factors = 1
    for n in factors.values():
        num_factors *= n+1
    return num_factors

        
if "__main__" == __name__:
    for tri in triangle_num_gen():
        if num_divisors(tri) > 500:
            break
    print tri
