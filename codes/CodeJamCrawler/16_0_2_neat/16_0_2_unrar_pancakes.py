def flip(n,L):
    for i in range(n):
        L[i] = not L[i]
    for i in range(n//2):
        L[i], L[n-(i+1)] = L[n-(i+1)], L[i]

def start(L):
    for i in range(len(L)):
        if not L[i]:
            return i

t = int(input())
for i in range(t):
    T = list(input())
    L = [t=='+' for t in T]
    c = 0
    while(not all(L)):
        if not L[len(L)-1]:
            k = start(L)
            if k == 0:
                k = len(L)
            if True in L:
                flip(k, L)
            else:
                c += 1
                break
            c += 1
        else:
            last = len(L)-L[::-1].index(False)
            L = L[:last]
    print("Case #"+str(i+1)+": "+str(c))


