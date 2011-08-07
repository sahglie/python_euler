#!/opt/local/bin/python


if "__main__" == __name__:
    fd = open("data.txt")
    n = sum([long(line.strip()) for line in fd.readlines()])
    fd.close()
    print str(n)[0:10]
