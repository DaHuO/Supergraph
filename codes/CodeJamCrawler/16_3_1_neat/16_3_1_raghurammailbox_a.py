T=int(raw_input())

cha=['A','B','C','D']

for t in range(0,T):
    N=int(raw_input())
    sen=map(int, raw_input().split())
    c=''
    while(sum(sen)>0):
        
        for sel1 in range(0,N):
            for sel2 in range(0,N):

                if(sen[sel1]==0): continue
                if(sen[sel2]==0):continue
                
                tem=sen[:]
                tem[sel1]=tem[sel1]-1
                tem[sel2]=tem[sel2]-1

                tot=sum(tem)/2
                flag=0
                for i in range(0,N):
                    if (tem[i]>tot):
                        flag=1
                        break
                if(flag==1):
                    for sel3 in range(0,N):
                        if(sen[sel3]==0): continue
                        tem2=sen[:]
                        tem2[sel3]=tem2[sel3]-1
                        flag2=0
                        tot2=sum(tem2)/2
                        for j in range(0,N):
                            if (tem2[j]>tot2):
                                flag2=1
                                break
                        if(flag2==0):
                            c=c+' '+cha[sel3]
                            sen=tem2[:]
                            break
                            

                else:
                    sen=tem[:]
                    c=c+' '+cha[sel1]+cha[sel2]

                
    print 'Case #'+str(t+1)+': '+c
