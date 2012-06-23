#!/opt/local/bin/python

"""The fraction 49/98 is a curious fraction, as an inexperienced mathematician
in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which
is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction,
less than one in value, and containing two digits in the numerator and
denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
"""

from fractions import Fraction

if __name__ == "__main__":
    fractions = []
    for n in xrange(10, 100):
        for d in xrange(n, 100):
            n1, n2 = n / 10, n % 10
            d1, d2 = d / 10, d % 10
            if d2 != 0 and n2 == d1 and n2 != n1:
                f = Fraction(n, d)
                g = Fraction(n1, d2)
                if f == g:
                    fractions.append(f)
    product = Fraction(1, 1)
    for f in fractions:
        product *= f
    print product.denominator
