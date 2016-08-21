import itertools
import math

num = input()

bits, cnt = map(int, raw_input().split())
print 'Case #1:'
for test in itertools.product(['0','1'], repeat=bits - 2):
    denoms = []
    test = ['1'] + list(test) + ['1']
    for base in range(2, 11):
        b = 1
        num = 0
        for t in test[::-1]:
            if t == '1':
                num += b
            b *= base
        for i in range(2, min(num - 1, int(math.sqrt(num))  )):
            if num % i == 0:
                denoms.append(i)
                break
        else:
            break
    else:
        print ''.join(test), ' '.join(map(str, denoms))
        cnt -= 1
        if cnt == 0:
            break




