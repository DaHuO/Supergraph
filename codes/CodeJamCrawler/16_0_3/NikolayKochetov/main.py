fin = open('input.txt')
fout = open('output.txt', 'w')
T = int(fin.readline())

for test in range(T):
    fout.write('Case #{0}: '.format(test + 1))
    # print(fin.readline().split())
    fout.write('\n')
    l, c = map(int, fin.readline().split())
    div = [i ** (l // 2) + 1 for i in range(2, 11)]
    for i in range(c):
        s = '{0:b}'.format(i)
        part = '1' + ('0' * (l // 2 - 2 - len(s))) + s + '1'
        fout.write(part + part + ' ' + ' '.join(map(str, div)) + '\n')

