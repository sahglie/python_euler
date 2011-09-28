#!/opt/local/bin/python

import re
import sys

"""If the numbers 1 to 5 are written out in words:
one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example:

342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British
usage.
"""


ONES = ["", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine"]

TEENS = ["ten", "eleven", "twelve", "thirteen", "fourteen",
         "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

TENS = ["", "", "twenty", "thirty", "forty",
        "fifty", "sixty", "seventy", "eighty", "ninety"]


def number_2_word(n):
    n = str(n)
    if len(n) == 1:
        return ONES[int(n)]
    elif len(n) == 2:
        pattern = re.compile(r'(\d+)(\d{1})')
        m = re.search(pattern, n)
        if m.groups()[0] == "1":
            return TEENS[int(m.groups()[1])]
        else:
            return "%s%s" % (TENS[int(m.groups()[0])], ONES[int(m.groups()[1])])
    elif len(n) == 3:
        pattern = re.compile(r'(\d+)(\d{2})')
        m = re.search(pattern, n)
        if m.groups()[1] == "00":
            return "%s hundred %s" % (ONES[int(m.groups()[0])], number_2_word(m.groups()[1]))
        else:
            return "%s hundred and %s" % (ONES[int(m.groups()[0])], number_2_word(m.groups()[1]))
    else:
        return "one thousand"

if __name__ == "__main__":
    words = [number_2_word(n) for n in xrange(1, 1001)]
    print len("".join(words).replace("-", "").replace(" ", ""))
        
