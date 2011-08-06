#!/opt/local/bin/python


"""By listing the first six prime numbers:

2, 3, 5, 7, 11, and 13,

we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

def nth_prime(n):
    D = {}
    q = 2
    i = 1
    while i <= n:
        if q not in D:
            i += 1
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(q + p, []).append(p)
            del D[q]
        q += 1
        
    return q-1

if "__main__" == __name__:
    print nth_prime(10001)

