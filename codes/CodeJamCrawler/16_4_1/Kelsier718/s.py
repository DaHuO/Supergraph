def valid(data,res):
    p = sum(1 for i in res if i=='P')
    r = sum(1 for i in res if i=='R')
    s = sum(1 for i in res if i=='S')
    return data[0]==p and data[1]==r and data[2]==s

def ty(w):
    tmp = ['P','R','S']
    return tmp[w]

def ch(l):
    if l=='P':
        return 'PR'
    if l=='R':
        return 'RS'
    if l=='S':
        return 'PS'

def solve(N,d,w):
    if N==1:
        return w
    tmp = ch(w)
    res = ''
    arr=[0]*2
    for j in range(2):
        arr[j] = solve(N/2,d,tmp[j])
    if arr[0] < arr[1]:
        return arr[0]+arr[1]
    else:
        return arr[1]+arr[0]

t = int(input())
for i in range(1, t + 1):
    N, R, P, S = [int(s) for s in input().split(" ")]
    d=[P,R,S]
    res1 = solve(2**N,d,'P')
    res2 = solve(2**N,d,'R')
    res3 = solve(2**N,d,'S')
    if valid(d,res1):
        res = res1
    else:
        if valid(d,res2):
            res = res2
        else:
            if valid(d,res3):
                res = res3
            else:
                res = 'IMPOSSIBLE'
    print("Case #{}: {}".format(i, res))
