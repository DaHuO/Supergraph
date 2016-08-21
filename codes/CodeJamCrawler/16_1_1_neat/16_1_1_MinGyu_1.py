tcase = input()

def add(arr, c):
    if arr is None:
        return c

    if len(arr) > 0 and arr[0] <= c:
        return c + arr
    else:
        return arr + c

def res(s):
    return reduce(add, s)

for case in xrange(1, tcase+1):

    print "Case #{}: {}".format(case, res(raw_input()))
