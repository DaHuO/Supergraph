from sys import *
f_i = open(argv[1])
f_o = open(argv[2], 'w')
cases = int(f_i.readline() [:-1])
for s in range(1, cases + 1):
    header = 'Case #' + str(s) + ': '
    string = f_i.readline() [:-1]
    k,c,s = [int(n) for n in string.split(' ')]
    if k == 1:
        if s < 1:
            output = 'IMPOSSIBLE'
        else:
            output = '1'
    elif c == 1:
        if s < k:
            output = 'IMPOSSIBLE'
        else:
            output = ' '.join([str(j) for j in range(1, k + 1)])
    elif s < k - 1:
        output = 'IMPOSSIBLE'
    else:
        output = ' '.join([str(j) for j in range(2, k + 1)])
    f_o.write(header + output + '\n')
f_o.close()
