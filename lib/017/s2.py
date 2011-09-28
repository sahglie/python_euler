#!/opt/local/bin/python

ONES = ["", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine"]

TEENS = ["ten", "eleven", "twelve", "thirteen", "fourteen",
         "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

TENS = ["", "", "twenty", "thirty", "forty",
        "fifty", "sixty", "seventy", "eighty", "ninety"]

def number_2_word(n):
    n = str(n).rjust(4, "0")
    thousands, hundreds, tens, ones = int(n[0]), int(n[1]), int(n[2]), int(n[3])
    teens = (n[2] == "1") and int(n[2])
    
    word = []
    if thousands:
        word.append("one thousand")
    if hundreds:
        word.append("%s hundred " % ONES[hundreds])
        if teens or tens or ones:
            word.append("and ")
    if teens:
        word.append(TEENS[ones])
        return "".join(word)
    if tens:
        word.append(TENS[tens])
    if ones:
        word.append(ONES[ones])
    
    return "".join(word)

if __name__ == "__main__":
    words = [number_2_word(n) for n in xrange(1, 1001)]
    print len("".join(words).replace("-", "").replace(" ", ""))
