import sys

ouf = open('/Users/sigma/Documents/output.txt', 'w')

n, k = 32, 500

print('Case #1:', file=ouf)
for i in range(1 << (n - 2)):
    good = True
    for a in range(2, 11):
        x = a ** (n - 1) + 1 + sum([a ** j for j in range(1, n - 1) if (i >> (j - 1)) & 1])
        if x % (a + 1) != 0:
            good = False
            break
    if good:
        print('1{}1 {}'.format(bin(i)[2:].zfill(n - 2), ' '.join([str(a + 1) for a in range(2, 11)])), file=ouf)
        k -= 1
        if k == 0:
            break