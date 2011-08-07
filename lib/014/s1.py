#!/opt/local/bin/python


"""The following iterative sequence is defined for the set of positive
integers:

n ->  n/2 (n is even)
n ->  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def chain_length(n, cache={}):
    if cache.has_key(n):
        return cache[n]
    elif n == 1:
        return 1
    elif n % 2 == 0:
        n /= 2
        l = chain_length(n, cache)
        cache[n] = l
        return l + 1
    else:
        n = (3 * n) + 1
        l = chain_length(n, cache)
        cache[n] = l
        return l + 1

if "__main__" == __name__:
    longest_chain = (0, 0)
    for i in range(1, 1000000):
        l = chain_length(i)
        if l > longest_chain[1]:
            longest_chain = (i, l)

    print longest_chain[0]
