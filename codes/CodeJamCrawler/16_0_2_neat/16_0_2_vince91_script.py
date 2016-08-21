T = int(raw_input())


def flip(arr, k):
    for i in xrange(k + 1):
        arr[i] = '+' if arr[i] == '-' else '-'


def solve(arr):
    count = 0
    for i in xrange(len(arr)-1, -1, -1):
        if arr[i] == '-':
            count += 1
            flip(arr, i)
    return count

for i in xrange(T):
    arr = [c for c in raw_input()]
    print("Case #%d: %s" % (i+1, solve(arr)))
