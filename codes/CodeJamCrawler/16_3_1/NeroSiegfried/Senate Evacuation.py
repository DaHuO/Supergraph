f = open('Senate Evacuation.txt', 'w')
T = int(raw_input())
for j in range(T):
    N = int(raw_input())
    P = [int(x) for x in raw_input().split()]
    f.write('Case #'+str(j+1)+': ')
    m1=[0,0]
    m2=[0,0]
    for i in range(len(P)):
        if P[i]>=m1[0]:
            m2=m1
            m1=[P[i],i]
        elif P[i]>=m2[0]:
            m2=[P[i],i]
    for i in range(m1[0]-m2[0]):
        f.write(str(chr(m1[1]+65))+' ')
    m=m2[0]
    m1[0]=0
    m2[0]=0
    for i in range(len(P)):
        if i== m1[1] or i== m2[1]:
            continue
        else:
            z=P[i]
            print P[i]
            while z > 0:
                f.write(str(chr(P.index(P[i])+65))+' ')
                print z
                z-=1
    for i in range(m):
        f.write(str(chr(m1[1]+65))+str(chr(m2[1]+65))+' ')
    f.write('\n')
               
        
            
