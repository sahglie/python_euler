#!/opt/local/bin/python

"""The nth term of the sequence of triangle numbers is given by,
Tn = 1/2(n)(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to
its alphabetical position and adding these values we form a word
value. For example, the word value for SKY is 19 + 11 + 25 = 55 = T10.
If the word value is a triangle number then we shall call the word
a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K
text file containing nearly two-thousand common English words, how
many are triangle words?
"""

# from string import ascii_lowercase

def letter_value(l):
    return ord(l.lower()) - 96

def triangle_numbers_upto(limit):
    triangles = set()
    t, n = 0, 1
    while t <= limit:
        t = (n*(n+1))/2
        triangles.add(t)
        n += 1
    return triangles
    

if __name__ == "__main__":
    triangle_words = 0
    words = []
    max_len = 0
    with open("words.txt") as f:
        data = f.read().strip().split(",")
        for w in data:
            word = w[1:-1]
            if len(word) > max_len:
                max_len = len(word)
            words.append(word)
        max_value = max_len * letter_value("z")
        triangles_numbers = triangle_numbers_upto(max_value)
        for word in words:
            if sum(letter_value(l) for l in word) in triangles_numbers:
                triangle_words += 1
        print triangle_words
