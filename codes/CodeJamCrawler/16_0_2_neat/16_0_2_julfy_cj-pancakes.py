from sets import Set

def count(n):
    sum = 0
    d = 1 if n[0] == '-' else 0
    prev = ''
    for c in n:
        if prev != c:
            sum += d
            d = 1
        prev = c
    return sum

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n = raw_input()
    #n,m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    print "Case #{}: {}".format(i, count(n[::-1]))
    # check out .format's specification for more formatting options
