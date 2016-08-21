T = int(input())

best = 0

def valid(l):
    global K
    
    l = l + [l[0]]
    for i in range(len(l)-1):
        x = l[i]
        if K[x] not in (l[i-1], l[i+1]):
            return False
    
    return True

def validb(l):
    if len(l) < 3:
        return True

    for i in range(1, len(l)-1):
        x = l[i]
        if K[x] not in(l[i-1], l[i+1]):
            return False

    return True

def rec(l):
    global N
    global K
    global best

    #print("rec", l)
    if valid(l):
        #print("valid", l)
        best = max(best, len(l))
    
    if len(l) == N:
        if valid(l):
            best = N
            #print("returning true")
            return True

    if validb(l):
        #print("validb", l)
        for i in range(N):
            if i not in l:
                if rec(l + [i]):
                    return True

    return False

for t in range(T):

    best = 0

    N = int(input())
    K = list(map(lambda x: int(x)-1, input().strip().split(' ')))

    for i in range(N):
        if rec([i]):
            break

    print("Case #" + str(t+1) + ": " + str(best))
