def solve(length, count):
    def get_divisor(x, lim):
        d = 2
        while d ** 2 <= x and d <= lim:
            if x % d == 0:
                return d
            d += 1
        return 0

    def gen_next(arr):
        arr[0] += 1
        for i in range(len(arr) - 1):
            arr[i + 1] += arr[i] // 2
            arr[i] %= 2
    
    ans = []
    arr = [0] * (length - 2)
    while len(ans) < count:
        s = '1' + ''.join((str(e) for e in reversed(arr))) + '1'
        divs = []
        for base in range(2, 11):
            divisor = get_divisor(int(s, base), 1000)
            if divisor == 0:
                break
            divs.append(divisor)
        else:
            ans.append(s + ' ' + ' '.join((str(e) for e in divs)))
        gen_next(arr)
    
    return '\n'.join(ans)    

import sys
sys.stdin = open('in', 'r')
sys.stdout = open('out', 'w')

t = int(input())
for i in range(1, t + 1):
    a, b = map(int, input().split())
    print('Case #%d:' % i)
    print(solve(a, b))

sys.stdin.close()
sys.stdout.close()
