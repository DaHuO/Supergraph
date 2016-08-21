import itertools
def find_answer():
    stds=[x for x in range(1,N+1)]
    for i in range(N+1,1,-1):
        combos=itertools.combinations(stds,i)
        for combo in combos:
            permus=itertools.permutations(combo)
            for permu in permus:
                if check(list(permu)): return i
    return 1

def check(arrange):
    if bffs[arrange[0]-1]!=arrange[1] and bffs[arrange[0]-1]!=arrange[-1]: return False
    if bffs[arrange[-1]-1]!=arrange[0] and bffs[arrange[-1]-1]!=arrange[-2]: return False
    for i in range(1,len(arrange)-1):
        if bffs[arrange[i]-1]!=arrange[i+1] and bffs[arrange[i]-1]!=arrange[i-1]: return False
    return True

T=int(input())
N=0
bffs=[]
for t in range(T):
    N=int(input())
    bffs=list(map(int,input().split()))
    print("Case #"+str(t+1)+": "+str(find_answer()))
