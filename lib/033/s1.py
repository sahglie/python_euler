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
            nr, nl = n % 10, n / 10
            dr, dl = d % 10, d / 10
            if dr != 0 and nr == dl and nr != nl:
                f = Fraction(n, d)
                g = Fraction(nl, dr)
                if f == g:
                    fractions.append(f)
    product = Fraction(1, 1)
    for f in fractions:
        product *= f
    print product.denominator
