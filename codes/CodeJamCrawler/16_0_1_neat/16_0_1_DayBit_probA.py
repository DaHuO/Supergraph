'''
Created on Apr 9, 2016

@author: david
'''
#f=open("exampleA.txt")
#f=open("A-small-attempt0.in")
f=open("A-large.in")

T=int(f.readline())
P=[]
for i in range(T):
    p = int(f.readline())
    P.append(p)

def solve(n):
    d=[True]*255
    nf = 10
    i=1
    #pre = -1
    last = -2
    while nf>0 and n!=0: #pre!=last:
        #pre = last
        last = i*n
        i += 1
        for dig_ in str(last):
            dig = ord(dig_)
            if d[dig]:
                d[dig]=False
                nf -= 1
    if nf>0:
        return "INSOMNIA"
    return (i-1)*n
       
fRes = open("res.txt", "w")
case=0
for p in P:
    print(p)
    case+=1
    sol = solve(p)
    print("Case #{}: {}".format(case,sol))
    fRes.write("Case #{}: {}\n".format(case,sol))
        
fRes.close()