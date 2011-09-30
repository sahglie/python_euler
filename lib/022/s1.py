#!/opt/local/bin/python

import re

"""Using names.txt, a 46K text file containing over five-thousand first
names, begin by sorting it into alphabetical order. Then working out the
alphabetical value for each name, multiply this value by its alphabetical
position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which
is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
COLIN would obtain a score of 938  53 = 49714.

What is the total of all the name scores in the file?
"""

def name_value(position, word):
    return sum(ord(c) - 64 for c in word) * position

if __name__ == "__main__":
    with open("names.txt") as f:
        names = sorted(name[1:-1] for name in f.read().strip().split(","))
        print sum(name_value(i+1, name) for i, name in enumerate(names))

