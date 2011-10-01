#!/opt/local/bin/python


"""Let d(n) be defined as the sum of proper divisors of
n(numbers less than n which divide evenly into n).

If d(a) = b and d(b) = a, where a  b, then a and b are an
amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are

1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284.

The proper divisors of 284 are
1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def divisors(n, cache):
    digits = []
    for i in xrange(1, (n/2)+1):
        if not n % i:
            digits.append(i)
    return digits
    
if "__main__" == __name__:
    amicables = set()
    cache = {}
    for n in xrange(1, 10001):
        d = sum(divisors(n, cache))
        if n == sum(divisors(d, cache)) and n != d:
            amicables.add(n)
    print sum(amicables)
            
