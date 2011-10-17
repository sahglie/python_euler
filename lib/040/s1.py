#!/opt/local/bin/python

"""An irrational decimal fraction is created by concatenating the
positive integers:

             |
0.123456789101112131415161718192021...
             |

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the
value of the following expression.

d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000
"""

def find_nth_digit(n):
    digits = 0
    for i in xrange(1, n+1):
        digits += len(str(i))
        if digits == n:
            return int(str(i)[-1])
        elif digits > n:
            s = str(i)
            index = (len(s)-1) - (digits-n)
            return int(s[index])


if __name__ == "__main__":
    prod = 1
    for i in xrange(0, 7):
        prod *= find_nth_digit(10**i)
    print prod
