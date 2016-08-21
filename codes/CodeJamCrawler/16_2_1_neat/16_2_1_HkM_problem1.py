def foo(I):
    J=[]
    while 'Z' in I:
        J.append(0)
        I.remove('Z')
        I.remove('E')
        I.remove('R')
        I.remove('O')
    while 'W' in I:
        J.append(2)
        I.remove('T')
        I.remove('W')
        I.remove('O')
    while 'U' in I:
        J.append(4)
        I.remove('F')
        I.remove('O')
        I.remove('U')
        I.remove('R')
    while 'X' in I:
        J.append(6)
        I.remove('S')
        I.remove('I')
        I.remove('X')
    while 'G' in I:
        J.append(8)
        I.remove('E')
        I.remove('I')
        I.remove('G')
        I.remove('H')
        I.remove('T')
    while 'O' in I:
        J.append(1)
        I.remove('O')
        I.remove('N')
        I.remove('E')
    while 'R' in I:
        J.append(3)
        I.remove('T')
        I.remove('H')
        I.remove('R')
        I.remove('E')
        I.remove('E')
    while 'F' in I:
        J.append(5)
        I.remove('F')
        I.remove('I')
        I.remove('V')
        I.remove('E')
    while 'V' in I:
        J.append(7)
        I.remove('S')
        I.remove('E')
        I.remove('V')
        I.remove('E')
        I.remove('N')
    while 'I' in I:
        J.append(9)
        I.remove('N')
        I.remove('I')
        I.remove('N')
        I.remove('E')
    J.sort()
    J=map(str,J)
    return ''.join(J)
n=input()
I=[]
for k in range(n):
    I.append(list(raw_input()))
k=1;
while k<=n:
    print 'Case #'+str(k)+': '+foo(I[k-1]);
    k+=1;
