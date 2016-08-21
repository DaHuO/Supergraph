'''
Created on Apr 9, 2016

@author: david
'''
#f=open("exampleD.txt")
f=open("D-small-attempt0.in")
#f=open("D-large.in")

T=int(f.readline())
P=[]
for i in range(T):
    p = [int(x) for x in f.readline().split()]
    P.append(p)

def solve(p):
    k,c,s = p
    if s<k: return "IMPOSSIBLE"
    return ' '.join([str(x) for x in range(1,s+1)])
       
fRes = open("res.txt", "w")
case=0
for p in P:
    print(p)
    case+=1
    sol = solve(p)
    print("Case #{}: {}".format(case,sol))
    fRes.write("Case #{}: {}\n".format(case,sol))
        
fRes.close()