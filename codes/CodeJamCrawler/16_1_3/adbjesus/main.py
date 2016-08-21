MAX = 0

def rec(i,N,L,C,bestie):
    global MAX
   
    if(len(C)>MAX):
        # Check if valid
        valid = True
        for i in range(len(C)):
            if L[C[i]-1]!=C[(i-1)%len(C)] and L[C[i]-1]!=C[(i+1)%len(C)]:
                valid=False
                break

        if valid:
            MAX=len(C)
    
    if(i==N):
        return

    if bestie == False:
        if L[C[-1]-1] not in C:
            rec(i+1,N,L,C+[L[C[-1]-1]],L[C[-1]-1]==C[-1])
        
        for j in range(len(L)):
            if L[j] == C[-1] and (j+1) not in C:
                rec(i+1, N, L, C+[j+1],True)

    if bestie == True:
        for j in range(len(L)):
            if (j+1) not in C:
                rec(i+1, N, L, C+[j+1],L[j]==C[-1])

def solve():
    global MAX
    MAX = 0
    N = input()
    L = [int(i) for i in raw_input().split()]
    for i in range(1,N+1):
        rec(1,N,L,[i],True)

T = input()

for t in range(1,T+1):
    solve()
    print("Case #%d: %d" % (t,MAX))
