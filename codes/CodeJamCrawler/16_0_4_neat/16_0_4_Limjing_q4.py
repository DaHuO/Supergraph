def grpy(K, C):
    ans = 0
    for i in range(C):
        #print K**i
        ans+=K**i
    return ans

def things (start, end, K, C):
    ans = 1
    if (start+C-1 <= end):
        for i in range(C):
            nb4 = start+i-1
            ans+=(nb4*K**i)
    else:
        i = -1
        for j in range(C):
            if (start+j-1<end):
                i+=1
            nb4 = start+i-1
            #print (nb4*K**j)
            ans+=(nb4*K**j)
    return ans

def solve_4(K, C, S):
    ans = []
    if (S>=K):
        for i in range(K):
            n_b4 = i
            grp = grpy(K, C)
            ans.append(str(n_b4*grp+1))
    elif (S*C>=K):
        for i in range(S):
            start = i*C+1
            end = min(start+C,K)
            if (start<K**C):
                ans.append(str(things(start, end, K, C)))
    else:
        return ['IMPOSSIBLE']
    return ans


nCases = int(raw_input())
for i in range(nCases):
    k, c, s = map(int, raw_input().split())
    print "Case #"+str(i+1)+": "+" ".join(solve_4(k, c, s))

for i in range(5):
    #print grpy(i, 3)
    pass

#print solve_4(3, 2, 3)
#print solve_4(5, 2, 5)
#print things(1, 3, 5, 3)
#print things(4, 5, 5, 3)
