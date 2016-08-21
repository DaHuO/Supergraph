File=open("B-large.txt",'w')

T=int(raw_input())
for t in range(T):
    N=int(raw_input())
    Heights=[]
    for n in range(2*N-1):
        paper=[int(h) for h in raw_input().split()]
        Heights.extend(paper)
    lost_paper=[]
    for h in Heights:
        if not Heights.count(h)%2==0:
            if not h in lost_paper:
                lost_paper.append(h)
    lost_paper.sort()
    Lost_paper=[]
    for h in lost_paper:
        Lost_paper.append(str(h))
        if not len(Lost_paper)==2*len(lost_paper)-1:
            Lost_paper.append(' ')
    y=''.join(Lost_paper)
    print >> File, "Case #%d: %s" %(t+1,y)
File.close()
