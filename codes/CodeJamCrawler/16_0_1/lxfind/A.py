import sys

def calculate(n):
    if n == 0:
        return 'INSOMNIA'
    a = [False] * 10
    cnt = 0
    cur = n
    while cnt < 10:
        tmp = cur
        while tmp > 0:
            x = tmp % 10
            if not a[x]:
                a[x] = True
                cnt += 1
            tmp /= 10
        cur += n
    return cur - n

input_file = sys.argv[1]
with open(input_file, 'r') as f:
    t = int(f.readline())
    for i in range(0, t):
        n = int(f.readline())
        print('Case #%d: %s' % ((i + 1), str(calculate(n))))
