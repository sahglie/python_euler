#!/opt/local/bin/python

D = {
    1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six",
    7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve",
    13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen",
    17:"seventeen", 18:"eighteen", 19:"nineteen", 20:"twenty",
    30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy",
    80:"eighty", 90:"ninety"
}

def number_2_word(n):
    n = str(n).rjust(4, "0")
    thousands, hundreds, tens, ones = int(n[0]), int(n[1]), int(n[2]), int(n[3])
    teens = (n[2] == "1") and int(n[2:])
    
    word = []
    if thousands:
        word.append("onethousand")
    if hundreds:
        word.append("%shundred" % D[hundreds])
        if teens or tens or ones:
            word.append("and")
    if teens:
        word.append(D[teens])
        return "".join(word)
    if tens:
        word.append(D[tens*10])
    if ones:
        word.append(D[ones])
    return "".join(word)


if __name__ == "__main__":
    print len("".join([number_2_word(n) for n in xrange(1, 1001)]))
