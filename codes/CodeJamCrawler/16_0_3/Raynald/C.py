import sys

f = sys.stdin
p = [2, 3, 5, 7]
for num in xrange(11, 2 ** 16):
    flag = True
    for pri in p:
        if num % pri == 0:
            flag = False
            break
    if flag:
        p += [num]
T = f.readline()
N, J = map(int, f.readline().strip().split(' '))
count = 0
print "Case #1:"
for num in xrange(2 ** (N - 1) + 1, 2 ** N, 2):
    p_list = []
    x = num
    s = ''
    while x > 0:
        if x % 2:
            s += '1'
        else:
            s += '0'
        x /= 2
    for res in xrange(2, 11):
        ans = 0
        for c in s:
            ans *= res
            if c == '1':
                ans += 1
        find = False
        for prime in p:
            if prime * prime > ans:
                break
            if ans % prime == 0:
                p_list += [str(prime)]
                find = True
                break
        if not find:
            break
    if len(p_list) == 9:
        count += 1
        print s, ' '.join(p_list)
        if count == J:
            break


