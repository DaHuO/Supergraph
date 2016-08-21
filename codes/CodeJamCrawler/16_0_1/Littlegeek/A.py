f = open('a.in', 'r')
o = open('ao.out', 'w')

T = f.readline()
C = 0
for line in f:
    C += 1
    s = '0123456789'
    n = int(line)
    i = 1
    if (n == 0):
        o.write("Case #" + str(C) +": INSOMNIA\n")
        s = ''
    while len(s)>0:
        for c in str(n*i):
            s = s.replace(c,'')
        if (len(s) == 0):
            o.write("Case #" + str(C) + ": " + str(n*i) + '\n')
        else:
            i += 1
f.close()
o.close()
