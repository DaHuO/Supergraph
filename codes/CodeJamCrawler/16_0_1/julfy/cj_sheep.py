from sets import Set

def count(n):
    so_far = Set()
    i = 0
    while len(so_far) < 10:
        i +=1
        so_far.update(str(i * n))
    return i*n

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n = int(raw_input())
    #n,m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    print "Case #{}: {}".format(i, "INSOMNIA" if n == 0 else count(n))
    # check out .format's specification for more formatting options
