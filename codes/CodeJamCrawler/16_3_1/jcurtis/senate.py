def solve(arr):
    total = sum(arr)
    ans = []
    while total > 0:
        m = max(arr)
        c = arr.count(m)
        i = arr.index(m)
        arr[i] -= 1
        total -= 1
        s = chr(65 + i)
        if c == 2:
            i = arr.index(m)
            arr[i] -= 1
            total -=1
            s += chr(65 + i)
        for x in arr:
            if 2 * x > total:
                print arr
            assert(2 * x <= total)
        ans.append(s)
    return ' '.join(ans)

def test():
    assert(solve([2,2]) == 'AB AB')

if __name__ == '__main__':
    test()
    t = int(raw_input())
    for i in range(1, t+1):

        tmp = raw_input()
        arr = map(int, raw_input().strip().split(' '))
        ans = solve(arr)
        print "Case #%d: %s" % (i, ans)
