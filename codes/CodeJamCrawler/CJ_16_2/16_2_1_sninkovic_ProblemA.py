T = int(raw_input())

imena={0:"ZERO",1:"ONE",2:"TWO", 3:"THREE",4:"FOUR",5:"FIVE",6:"SIX",7:"SEVEN",8:"EIGHT",9:"NINE"}
for t in range(0,T):
    mapa={}
    input = raw_input()
    mapa={'Z':0,'G':0,'W':0,'X':0,'H':0,'R':0,'F':0,'V':0,'I':0,'O':0}
    for i in input:
        if mapa.has_key(i):
            mapa[i] = mapa[i]+1
        else:
            mapa[i]=1
    rv=[]


    while mapa['Z']>0:
        rv.append(0)
        for a in imena[0]:
            mapa[a]=mapa[a]-1
  
    while mapa['G']>0:
        rv.append(8)
        for a in imena[8]:
            mapa[a]=mapa[a]-1
    while mapa['W']>0:
        rv.append(2)
        for a in imena[2]:
            mapa[a]=mapa[a]-1
    while mapa['X']>0:
        rv.append(6)
        for a in imena[6]:
            mapa[a] = mapa[a]-1
    while mapa['H']>0:
        rv.append(3)
        for a in imena[3]:
            mapa[a]=mapa[a]-1
    while mapa['R']>0:
        rv.append(4)
        for a in imena[4]:
            mapa[a] = mapa[a]-1
    while mapa['F']>0:
        rv.append(5)
        for a in imena[5]:
            mapa[a] = mapa[a]-1
    while mapa['V']>0:
        rv.append(7)
        for a in imena[7]:
            mapa[a]=mapa[a]-1
    while mapa['I']>0:
        rv.append(9)
        for a in imena[9]:
            mapa[a]=mapa[a]-1
    while mapa['O']>0:
        rv.append(1)
        for a in imena[1]:
            mapa[a]=mapa[a]-1

    print "Case #"+str(t+1)+":","".join(map(str,sorted(rv)))
            
            
