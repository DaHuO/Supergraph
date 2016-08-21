input=open("A-large.in","r")
output=open("PAlarge.txt","w")

T = int(input.readline())

for loop in range(T):
    S = list(input.readline())
    res = []
    
    while S!=['\n']:
        while 'Z' in S:
            res.append(0)
            S.remove('Z')
            S.remove('E')
            S.remove('R')
            S.remove('O')
        while 'W' in S:
            res.append(2)
            S.remove('T')
            S.remove('W')
            S.remove('O')
        while 'X' in S:
            res.append(6)
            S.remove('S')
            S.remove('I')
            S.remove('X')
        while 'G' in S:
            res.append(8)
            S.remove('E')
            S.remove('I')
            S.remove('G')
            S.remove('H')
            S.remove('T')
        while 'H' in S:
            res.append(3)
            S.remove('T')
            S.remove('H')
            S.remove('R')
            S.remove('E')
            S.remove('E')
        while 'S' in S:
            res.append(7)
            S.remove('S')
            S.remove('E')
            S.remove('V')
            S.remove('E')
            S.remove('N')
        while 'R' in S:
            res.append(4)
            S.remove('F')
            S.remove('O')
            S.remove('U')
            S.remove('R')
        while 'V' in S:
            res.append(5)
            S.remove('F')
            S.remove('I')
            S.remove('V')
            S.remove('E')
        while 'O' in S:
            res.append(1)
            S.remove('O')
            S.remove('N')
            S.remove('E')
        while 'I' in S:
            res.append(9)
            S.remove('N')
            S.remove('I')
            S.remove('N')
            S.remove('E')
        
    res.sort()
        
    trueres = ''
    for i in res:
        trueres += str(i)
        
    output.write("Case #{}: {}\n".format(loop+1,trueres))

input.close()
output.close()