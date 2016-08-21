def read():
    T = int(input())
    case = []
    for i in range(0,T):
        case.append(input())
    for i in range(0,T):
        compute(case[i],i+1)

def compute(pile, n):
    h = len(pile)
    count = 0
    pos = 0
    cur = pile[0]
    while pos < h:
        if pile[pos] == cur:
            pos = pos + 1
            continue
        count = count + 1
        cur = pile[pos]
        pos = pos + 1
    if cur == '-':
        count = count + 1
    print ('Case #'+str(n)+': '+str(count))

read()
