inf = open('input.txt', 'r')
ouf = open('output.txt', 'w')
t = int(inf.readline())
for i in range(1, t + 1):
    n = int(inf.readline())
    if n == 0:
        print('Case #{}: INSOMNIA'.format(i), file=ouf)
    else:
        digits = set()
        for j in range(1, 10 ** 6):
            digits.update(set(str(n * j)))
            if len(digits) == 10:
                print('Case #{}: {}'.format(i, n * j), file=ouf)
                break
        
inf.close()
ouf.close()