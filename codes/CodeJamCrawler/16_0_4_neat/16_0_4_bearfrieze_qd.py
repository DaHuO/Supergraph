import fileinput

f = fileinput.input()
T = int(f.readline())

for case in range(1, T + 1):
    K, C, S = [int(s) for s in f.readline().strip('\n').split(' ')]
    print('Case #%d: %s' % (case, ' '.join(str(i) for i in range(1, S + 1))))
