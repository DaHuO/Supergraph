def readint(): return int(raw_input())
def readarray(f): return map(f, raw_input().split())

MAX_INT = 999999
_T = readint()

for _t in range(_T):
    N = readint()
    digits_seen = []
    i = 1

    while len(digits_seen) < 10:
        digits = list(str(N*i))
        for d in digits:
            if d not in digits_seen:
                digits_seen.append(d)
        i = i+1
        
        if i == MAX_INT:
            print 'Case #%i: INSOMNIA'%(_t+1)
            break
        
    if i == MAX_INT:
        continue
    print 'Case #%i:'%(_t+1), N*(i-1)


