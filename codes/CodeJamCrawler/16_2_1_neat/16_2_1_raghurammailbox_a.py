T=int(raw_input())

for t in range(0,T):
    S=raw_input()
    S=list(S)
    zero=S.count('Z')
    two=S.count('W')
    for i in range(0,two):
        S.remove('O')

    four=S.count('U')
    for i in range(0,four):
        S.remove('O')
    for i in range(0,zero):
        S.remove('O')
        
    one=S.count('O')
    
    for i in range(0,one):
        S.remove('N')
    
    six=S.count('X')
    for i in range(0,six):
        S.remove('S')
    seven=S.count('S')
    for i in range(0,seven):
        S.remove('V')
        S.remove('N')
    five=S.count('V')

    eight=S.count('G')
    for i in range(0,eight):
        S.remove('H')
    three=S.count('H')
    nine=S.count('N')/2
    out=''
    for i in range(0,zero):
        out=out+'0'
    for i in range(0,one):
        out=out+'1'
    for i in range(0,two):
        out=out+'2'
    for i in range(0,three):
        out=out+'3'
    for i in range(0,four):
        out=out+'4'
    for i in range(0,five):
        out=out+'5'
    for i in range(0,six):
        out=out+'6'
    for i in range(0,seven):
        out=out+'7'
    for i in range(0,eight):
        out=out+'8'
    for i in range(0,nine):
        out=out+'9'

    print "Case #"+str(t+1)+": "+out
