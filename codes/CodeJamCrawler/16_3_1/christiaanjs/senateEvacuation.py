t = int(input())
parties = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def getMaxIndex(p):
    return p.index(max(p))

for c in range(t):
    plan = []
    n = int(input())
    p = list(map(int, input().split()))
    while not all([x==0 for x in p]):
        notEmpty = [x for x in p if x != 0]
        if (len(notEmpty) == 2 and notEmpty[0]-notEmpty[1] == 1) or (len(notEmpty) == 3 and sum(notEmpty) == 3):#If only 1 difference between two parties, only evacuate 1
            index = getMaxIndex(p)
            p[index] -= 1
            plan.append(parties[index])
        else:
            first = getMaxIndex(p)
            p[first] -= 1
            second = getMaxIndex(p)
            p[second] -= 1
            plan.append(parties[first] + parties[second])
    print("Case #{0}: {1}".format(c+1, " ".join(plan)))
          
            
                
            
            
                
                
            
    