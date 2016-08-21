from collections import deque
def Solution(i, line):
    a = deque([])
    for s in line:
        if not a:
            a.append(s)
        elif a[0] > s:
            a.append(s)
        else:
            a.appendleft(s)
    print "Case #{}: {}".format(i, "".join(a))
    return



if __name__ == '__main__':
    import sys

    file_name = sys.argv[1]
    with open(file_name) as f:
        line = f.readline()
        for i in xrange(1, int(line)+1):
            line = f.readline().strip('\n')
            Solution(i,line)