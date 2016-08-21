def readint(): return int(raw_input())
def readarray(f): return map(f, raw_input().split())

_T = readint()

for _t in range(_T):
    D = raw_input()
    n = int(D)
    r = list(D)
    r = list(set(r))
    i = 2
    while len(r)<10 and i < 999999:
        j= i*n
        nr  = list(str(j))    
        r = nr + r
        r = list(set(r))
        i = i+1

    if i == 999999:
        j = "INSOMNIA"    

    print 'Case #%i:'%(_t+1), j
