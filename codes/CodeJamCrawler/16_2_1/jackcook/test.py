import sys

fp = file(sys.argv[1], 'r')

t = int(fp.next())

of = file("out.txt", "w+")

for i in range(t):
    s = fp.next().strip()
    f = []
    while 'Z' in s:
        s = s.replace('Z', '', 1).replace('E', '', 1).replace('R', '', 1).replace('O', '', 1)
        f.append(0)
    while 'W' in s:
        s = s.replace('T', '', 1).replace('W', '', 1).replace('O', '', 1)
        f.append(2)
    while 'U' in s:
        s = s.replace('F', '', 1).replace('O', '', 1).replace('U', '', 1).replace('R', '', 1)
        f.append(4)
    while 'X' in s:
        s = s.replace('S', '', 1).replace('I', '', 1).replace('X', '', 1)
        f.append(6)
    while 'G' in s:
        s = s.replace('E', '', 1).replace('I', '', 1).replace('G', '', 1).replace('H', '', 1).replace('T', '', 1)
        f.append(8)
    while 'H' in s:
        s = s.replace('T', '', 1).replace('H', '', 1).replace('R', '', 1).replace('E', '', 1).replace('E', '', 1)
        f.append(3)
    while 'F' in s:
        s = s.replace('F', '', 1).replace('I', '', 1).replace('V', '', 1).replace('E', '', 1)
        f.append(5)
    while 'S' in s:
        s = s.replace('S', '', 1).replace('E', '', 1).replace('V', '', 1).replace('E', '', 1).replace('N', '', 1)
        f.append(7)
    while 'O' in s:
        s = s.replace('O', '', 1).replace('N', '', 1).replace('E', '', 1)
        f.append(1)
    while 'N' in s:
        s = s.replace('N', '', 1).replace('I', '', 1).replace('N', '', 1).replace('E', '', 1)
        f.append(9)
    f.sort()
    g = ''
    for n in f:
        g += str(n)
    of.write("Case #%d: %s\n" % (i + 1, g))

of.close()
