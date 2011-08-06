#!/opt/local/bin/python


def build_number():
    fd = open("data.txt")
    parts = [s.strip() for s in fd.readlines()]
    fd.close()
    return "".join(parts)


if "__main__" == __name__:
    number_str = build_number()
    prod_func = lambda x,y: x*y
    print max(reduce(prod_func, (int(n) for n in number_str[i:i+5]))
              for i in range(0, len(number_str)-5))
