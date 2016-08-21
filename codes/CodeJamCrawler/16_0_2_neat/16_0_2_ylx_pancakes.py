from sys import *
f_i = open(argv[1])
f_o = open(argv[2], 'w')
cases = int(f_i.readline() [:-1])
for s in range(1, cases + 1):
    flips = 0
    header = 'Case #' + str(s) + ': '
    string = f_i.readline() [:-1]
    for n in range(len(string) - 1):
        if string[n] != string[n+1]:
            flips += 1
    if string[-1] == '-':
        flips += 1
    f_o.write(header + str(flips) + '\n')
f_o.close()
