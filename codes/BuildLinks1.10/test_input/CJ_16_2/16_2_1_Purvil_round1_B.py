from collections import Counter
n=input()
l={'ZERO':'0','ONE':'1','TWO':'2','THREE':'3','FOUR':'4','FIVE':'5','SIX':'6','SEVEN':'7','EIGHT':'8','NINE':'9'}
for i in range(n):
    s=raw_input()
    s=list(s)
    p=[]
    while s!=[]:
        while 'Z' in s:
            if 'Z' in s:
                p.append(0)
                s.remove('Z')
                s.remove('E')
                s.remove('R')
                s.remove('O')
        while 'W' in s:
            if 'W' in s:
                p.append(2)
                s.remove('T')
                s.remove('W')
                s.remove('O')
        while 'U' in s:
            if 'U' in s:
                p.append(4)
                s.remove('F')
                s.remove('O')
                s.remove('U')
                s.remove('R')
        while 'G' in s:
            if 'G' in s:
                p.append(8)
                s.remove('E')
                s.remove('I')
                s.remove('G')
                s.remove('H')
                s.remove('T')
        while 'X' in s:
            if 'X' in s:
                p.append(6)
                s.remove('S')
                s.remove('I')
                s.remove('X')
        while 'O' in s and 'N' in s and 'E' in s:
            p.append(1)
            s.remove('O')
            s.remove('N')
            s.remove('E')
        while 'T' in s and 'H' in s and 'R' in s and 'E' in s and 'E' in (Counter(s) - Counter(['E'])):
            p.append(3)
            s.remove('T')
            s.remove('H')
            s.remove('R')
            s.remove('E')
            s.remove('E')
        while 'F' in s and 'I' in s and 'V' in s and 'E' in s:
            p.append(5)
            s.remove('F')
            s.remove('I')
            s.remove('V')
            s.remove('E')
        while 'S' in s and 'E' in s and 'V' in s and 'E' in (Counter(s) - Counter(['E'])) and 'N' in s:
            p.append(7)
            s.remove('S')
            s.remove('E')
            s.remove('V')
            s.remove('E')
            s.remove('N')
        while 'N' in s and 'I' in s and 'N' in (Counter(s) - Counter(['N'])) and 'E' in s:
            p.append(9)
            s.remove('N')
            s.remove('I')
            s.remove('N')
            s.remove('E')
    p.sort()
    ans=''
    for j in p:
        ans+=str(j)
    print 'Case #'+str(i+1)+': '+ans
