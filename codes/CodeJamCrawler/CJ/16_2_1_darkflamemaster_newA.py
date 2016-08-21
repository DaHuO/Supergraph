


T=int(input())
for i in range(T):
    dic={'Z':0,'E':0,'R':0,'O':0,'N':0,'W':0,'T':0,'H':0,'F':0,'I':0,'V':0,'S':0,'X':0,'G':0,'U':0}
    dic2=[0]*10
    S=input()
    for j in range(len(S)):
            dic[S[j]]=dic[S[j]]+1
    if 'W' in dic:
       dic2[2]=dic['W']
       dic['O'],dic['T']=dic['O']-dic['W'],dic['T']-dic['W']
       del dic['W']
    if 'Z' in dic:
        dic2[0]=dic['Z']
        dic['E']=dic['E']-dic['Z']
        dic['R']=dic['R']-dic['Z']
        dic['O']=dic['O']-dic['Z']
        del dic['Z']
    if 'G' in dic:
        dic2[8]=dic['G']
        dic['E']-=dic['G']
        dic['I']-=dic['G']
        dic['H']-=dic['G']
        dic['T']-=dic['G']
        del dic['G']
    if 'T' in dic:
        dic2[3]=dic['T']
        dic['H']-=dic['T']
        dic['R']-=dic['T']
        dic['E']-=dic['T']*2
        del dic['T']
    if 'R' in dic:
        dic2[4]=dic['R']
        dic['F']-=dic['R']
        dic['O']-=dic['R']
        dic['U']-=dic['R']
        del dic['R']
    if 'F' in dic:
        dic2[5]=dic['F']
        dic['I']-=dic['F']
        dic['V']-=dic['F']
        dic['E']-=dic['F']
        del dic['F']
    if 'V' in dic:
        dic2[7]=dic['V']
        dic['S']-=dic['V']
        dic['E']-=dic['V']*2
        dic['N']-=dic['V']
        del dic['V']
    if 'S' in dic:
        dic2[6]=dic['S']
        dic['I']-=dic['S']
        dic['X']-=dic['S']
        del dic['S']
    if 'I' in dic:
        dic2[9]=dic['I']
        dic['N']-=dic['I']*2
        dic['E']-=dic['I']
        del dic['I']
    if 'N' in dic:
        dic2[1]=dic['N']
        del dic['N']
    s=''
    for k in  range(10):
        s=s+str(k)*dic2[k]
    print('Case #'+str(i)+': '+s)
    
        
    
