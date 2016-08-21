from math import ceil

def get_index(L, H):
    t = []
    index = 0
    for i in L:
        if i >= H-1 and i > 0:
            t.append(index)
        index += 1
            
    return t

m = ['A', 'B', 'C']

def true_(L):
    for i in L:
        if i > 0:
            return True
        
    return False

for t in range(int(input())):
    N = int(input())
    L = list(map(int, input().split(" ")))
    H = ceil(sum(L) / len(L))
    res = []
    while true_(L):
        tmp = get_index(L, H)
        if len(tmp) == 1 or len(tmp) > 3:
            if tmp[0] > 1:
                L[tmp[0]] -= 2
                res.append(m[tmp[0]]+m[tmp[0]])
                H = ceil(sum(L) / len(L))
            else:
                L[tmp[0]] -= 1
                res.append(m[tmp[0]])
                H = ceil(sum(L) / len(L))
        elif len(tmp) == 2:
            L[tmp[0]] -= 1
            L[tmp[1]] -= 1
            res.append(m[tmp[0]]+m[tmp[1]])
            H -= 1
        elif len(tmp) == 3:
            if L[tmp[0]] == L[tmp[1]] == L[tmp[2]]:
                L[tmp[0]] -= 1
                res.append(m[tmp[0]])
                H = ceil(sum(L) / len(L))
            elif L[tmp[0]] == L[tmp[1]] and L[tmp[0]] > L[tmp[2]]:
                L[tmp[0]] -= 1
                L[tmp[1]] -= 1
                res.append(m[tmp[0]]+m[tmp[1]])
                H -= 1
            elif L[tmp[1]] == L[tmp[2]] and L[tmp[2]] > L[tmp[0]]:
                L[tmp[1]] -= 1
                L[tmp[2]] -= 1
                res.append(m[tmp[1]]+m[tmp[2]])
                H -= 1
            elif L[tmp[0]] == L[tmp[2]] and L[tmp[2]] > L[tmp[1]]:
                L[tmp[0]] -= 1
                L[tmp[2]] -= 1
                res.append(m[tmp[0]]+m[tmp[2]])
                H -= 1
            elif L[tmp[0]] > L[tmp[1]]:
                L[tmp[0]] -= 1
                L[tmp[2]] -= 1
                res.append(m[tmp[0]]+m[tmp[2]])
                H -= 1 
            else:
                L[tmp[1]] -= 1
                L[tmp[2]] -= 1
                res.append(m[tmp[1]]+m[tmp[2]])
                H -= 1    
                
    print("Case #"+str(t+1)+": "+' '.join(res))
            
        
