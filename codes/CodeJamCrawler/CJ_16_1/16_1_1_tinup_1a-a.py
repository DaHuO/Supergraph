import sys
sys.stdout = open("nout.txt", "w")
L=-1

def generate(s,t,st):
    global L
    if s=="":
        st.add(t)
        return
    c=s[0]
    a=t+str(c)
    b=str(c)+t
    if a>b:
        generate(s[1:],a,st)
    else:
        generate(s[1:],b,st)      
    

def solve(s):
    global L
    strs=set()
    L = len(s)
    t=""
    for c in s:
        a = t+str(c)
        b = str(c) + t
        if a>b:
            t= t+str(c)
        else:
            t= str(c)+t
    return t       
    

lines = []

with open("A-large.in", "r") as f:
    lines = f.readlines()

n = int(lines[0])

for i in range(1, n+1):
    ans = solve(lines[i].strip())
    print("Case #{}: {}".format(i, str(ans)))
