__author__ = 'gosu'

from math import log

def get_digits(x):
    rv = set([])
    while x:
        rv.add(int(x % 10))
        x //= 10
    return rv

def main():
    inp = open("input.in")
    c = int(inp.readline())
    casenum = 1
    for x in range(c):
        linestr = inp.readline().strip()
        n = int(linestr)
        if n == 0:
            print("Case #{0}: INSOMNIA".format(casenum))
        else:
            intset = set([])
            origin = n
            count = 1
            while len(intset) < 10:
                intset.update(get_digits(n))
                count += 1
                n = origin * count
                #print(intset)
            print("Case #{0}: {1}".format(casenum, origin * (count-1)))
        casenum += 1


if __name__ == '__main__':
    main()