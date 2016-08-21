from sys import *
f_i = open(argv[1])
f_o = open(argv[2], 'w')
cases = int(f_i.readline() [:-1])
for w in range(1, cases + 1):
    header = 'Case #' + str(w) + ': '
    string = f_i.readline() [:-1]
    res = ''
    for ch in string:
        if res == '' or ch >= res[0]:
            res = ch + res
        else:
            res += ch
    f_o.write(header + res + '\n')
f_o.close()
