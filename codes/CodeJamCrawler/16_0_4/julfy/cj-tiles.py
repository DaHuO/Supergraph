from sets import Set

def count(num,rec,stud):
    if num == 1:
        print 1;
        return;
    if rec == 1:
        if stud < num:
            print "IMPOSSIBLE"
        else:
            print " ".join(map(str,range(1,num+1)))
    else:
        if stud < (num-1):
            print "IMPOSSIBLE"
        else:
            print " ".join(map(str,range(2,num+1)))

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n,m,k = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    print "Case #{}:".format(i),
    count(n,m,k)
    # check out .format's specification for more formatting options
