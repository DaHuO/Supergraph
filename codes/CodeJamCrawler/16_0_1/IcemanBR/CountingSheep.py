import numpy as np

my_file = open('A-large.in', 'r')
T = int(my_file.readline())
digits = np.ones(10)

for i in range(1, T + 1):
    N = int(my_file.readline().strip())
    case = digits.copy()
    if N == 0:
        print 'Case #{0}: INSOMNIA'.format(i)
    else:
        j = 1
        while case.sum() > 0:
            n = N * j
            for x in map(int, str(n)):
                case[x] = 0
                print case
            if case.sum() == 0:
                print 'Case #{0}: {1}'.format(i, n)
            j += 1
            
my_file.close()
