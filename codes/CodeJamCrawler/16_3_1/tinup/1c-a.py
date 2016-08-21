def check(p):
    s =0 
    for pi in p:
        s+=pi
    for pi in p:
        if pi>s/2:
            return True
    return False
    
def checksum(p):
    s=0
    for pi in p:
        if pi<0:
            return True
        s+=pi
    if s==0:
        return False
    return True
        
def solve(p):
    ans =""
    
    while checksum(p):
        for i in range(len(p)):
            if p[i]>0:
                p[i]-=1
                while not check(p):
                    p[i]-=1
                    ans+="ABCDEFGHIJKLMNOPQRSTUVWXYZ"[i]+" "
                else:
                    if checksum(p):
                        p[i]+=1
            for j in range(i+1,len(p)):
                if p[i] and p[j]:
                    p[i]-=1
                    p[j]-=1
                    while not check(p):
                        p[i]-=1
                        p[j]-=1
                        t= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                        ans+=t[i]+t[j]+" "
                    else:
                        if checksum(p):
                            p[i]+=1
                            p[j]+=1
    return ans
            
    
    

lines = []

with open("A-small-attempt0.in", "r") as f:
    lines = f.readlines()

t = int(lines[0])
ctr=1
l=""
parties = [0]*26
for i in range(1, t+1):
    n=int(lines[ctr].strip())
    ctr+=1
    val = lines[ctr].strip().split()
    ctr+=1
    for j in range(n):
        parties[j] = int(val[j])
    ans = solve(parties)
    l+="Case #{}: {}\n".format(i, str(ans))

with open("out.txt","w") as f:
    f.write(l)
