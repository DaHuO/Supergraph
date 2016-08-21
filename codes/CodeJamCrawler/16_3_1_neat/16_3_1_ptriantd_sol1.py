import copy
f=open('A-large.in')
g=open('Result.in','w')
T=int(f.readline())
a='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(T):
    N=int(f.readline())
    members = list(map(int, f.readline().strip().split()))
    moves = []
    while sum(members)>0:
        m=max(members)
        maxind = [i for i, x in enumerate(members) if x == m]
        #print(members)
        #print(moves)
        #print(maxind)
        if len(maxind)==1:
            #print(members)
            if members[maxind[0]]>1:
                moves.append(a[maxind[0]]+a[maxind[0]])
                members[maxind[0]]-=2
            else:
                moves.append(a[maxind[0]])
                members[maxind[0]]=0
        else:
            temp_moves = copy.deepcopy(moves)
            temp_members = copy.deepcopy(members)
            #print(members)
            #print(temp_members)
            moves.append(a[maxind[0]]+a[maxind[1]])
            members[maxind[0]]-=1
            members[maxind[1]]-=1
            #print(members)
            #print(temp_members)
            m=max(members)
            #print(m)
            maxind = [i for i, x in enumerate(members) if x == m]
            #print(maxind)
            #print(members[maxind[0]])
            
            if len(maxind)==1 and members[maxind[0]]>sum(members)-members[maxind[0]]:
                #print('Entered')
                moves=temp_moves
                members=temp_members
                #print(moves)
                #print(members)
                m=max(members)
                maxind = [i for i, x in enumerate(members) if x == m]
                moves.append(a[maxind[0]])
                members[maxind[0]]-=1
       
    #print(moves)       
    g.write('Case #'+str(i+1)+':')
    for e in moves:
        g.write(' '+e)
    g.write('\n')
        
    
    
g.close()
f.close()
