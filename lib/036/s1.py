#!/opt/local/bin/python


"""The decimal number, 585 = 1001001001 (binary), is palindromic in both
bases.  Find the sum of all numbers, less than one million, which are
palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""

def is_b10_palidrome(n):
    n = str(n)
    return n == n[::-1]

def is_b2_palidrome(n):
    n = bin(n)[2:]
    return n == n[::-1]


if __name__ == "__main__":
    sum = 0
    for n in xrange(1, 1000000, 2):
        if is_b10_palidrome(n) and is_b2_palidrome(n):
            sum += n
    print sum
