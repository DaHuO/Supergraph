'''
Created on Apr 9, 2016

@author: david
'''
#f=open("exampleA.txt")
#f=open("A-small-attempt2.in")
f=open("A-large.in")

pp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

T=int(f.readline())
P=[]
for i in range(T):
    n = int( f.readline().strip() )
    line = f.readline().strip()
    words = line.split()
    ints = [int(w) for w in words]
    
    P.append(ints)

def solve(ns):
    res=[]
    esq = sum(ns)
    p = sorted([[n,pp[i]] for (i,n) in enumerate(ns)], reverse = True)
    while p[0][0]>1:
        if p[0][0] > p[1][0]:
            res.append(p[0][1])
            p[0][0] -= 1
        else:
            res.append(p[0][1]+p[1][1])
            p[0][0] -= 1
            p[1][0] -= 1
        p = sorted(p, reverse = True)
    while len(p)>2:
        res.append(p[0][1])
        del p[0]
    res.append(p[0][1]+p[1][1])
    #print (esq, p)
    return ' '.join(res)
       
fRes = open("res.txt", "w")
case=0
for p in P:
    print(p)
    case+=1
    sol = solve(p)
    print("Case #{}: {}".format(case,sol))
    fRes.write("Case #{}: {}\n".format(case,sol))
        
fRes.close()