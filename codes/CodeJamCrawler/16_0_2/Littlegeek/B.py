f = open('b.in', 'r')
o = open('bo.out', 'w')

f.readline()
C = 0
for line in f:
    C += 1
    if (line[0] == '-'):
        n = 1
    else:
        n = 0
    n += line.count('+-') * 2
    o.write('Case #' + str(C) + ': ' + str(n) + '\n')
f.close()
o.close()
