import sys
def check(arr):
    for i in arr:
        if(i == -1):
            return False
    return True

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    N = int(raw_input())  # read a list of integers, 2 in this case
    arr = [-1] * 10
    j = 1
    while True:
        n = j * N
        if (n == 0):
            print "Case #{}: {}".format(i,"INSOMNIA")
            break
        for ch in str(n):
            arr[int(ch)] = 1

        if(check(arr)):
            print "Case #{}: {}".format(i,n)
            break

        j = j + 1

