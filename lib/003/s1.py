#!/opt/local/bin/python

"""
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29. What is the 
largest prime factor of the number 600_851_475_143
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


def prime_factors(n):
    factors = []
    for prime in prime_gen():
        if n % prime == 0:
            factors.append(prime)
            n /= prime
        if n <= prime:
            break
    return factors
    

if __name__ == "__main__":
    print prime_factors(600851475143).pop()

