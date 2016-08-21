import sys

def digits(num):
    s = set()
    while num != 0:
        s.add(num % 10)
        num /= 10
    return s

f = open(sys.argv[1], 'r')
num = f.readline().strip()
for i in xrange(1, int(num)+1):
    N = int(f.readline())
    result = set()
    for m in range(1,1000):
        num = N * m
        result.update(digits(num))
        if len(result) >= 10:
            break
    ans = 'Case #'+str(i)+': '
    if len(result) < 10:
        ans += 'INSOMNIA'
    else:
        ans += str(num)
    print ans


