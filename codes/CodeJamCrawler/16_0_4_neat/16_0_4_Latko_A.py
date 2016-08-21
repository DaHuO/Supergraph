inf = open('input.txt', 'r')
ouf = open('output.txt', 'w')
t = int(inf.readline())

for test in range(1, t + 1):
    k, c, s = map(int, inf.readline())
    print('Case #{}: '.format(test) + ' '.join([str(i) for i in range(1, k + 1)]), file = ouf)

inf.close()
ouf.close()