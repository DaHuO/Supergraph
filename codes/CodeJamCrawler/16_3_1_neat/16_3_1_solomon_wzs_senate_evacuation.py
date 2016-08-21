#!/usr/bin/python2


def f(n, arr):
    cnt = float(sum(arr))
    ans = []
    while cnt > 0:
        if arr[0] > arr[1]:
            midx0 = 0
            midx1 = 1
        else:
            midx0 = 1
            midx1 = 0

        for i in xrange(2, n):
            if arr[i] >= arr[midx0]:
                midx1 = midx0
                midx0 = i
            elif arr[i] >= arr[midx1]:
                midx1 = i

        if cnt % 2 != 0:
            ans.append(chr(ord('A') + midx0))
            arr[midx0] -= 1
            cnt -= 1
        elif cnt > 2 and arr[midx1]/(cnt-2) <= 0.5:
            arr[midx0] -= 2
            ans.append(chr(ord('A') + midx0) * 2)
            cnt -= 2
        else:
            arr[midx0] -= 1
            arr[midx1] -= 1
            ans.append(chr(ord('A') + midx0) + chr(ord('A') + midx1))
            cnt -= 2
    return ans



import sys

fd = open(sys.argv[1], "rb")
T = int(fd.readline().strip())
for i in xrange(1, T + 1):
    n = int(fd.readline().strip())
    arr = [int(x) for x in fd.readline().strip().split(" ")]
    ans = f(n, arr)
    print "Case #%d: %s" % (i, ' '.join(ans))

fd.close()
