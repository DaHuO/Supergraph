def read():
    T = int(input())
    case = []
    for i in range(0,T):
        case.append(int(input()))
    for i in range(0,T):
        print('Case #'+str(i+1)+': '+str(compute(case[i])))

def compute(N):
    Seen = [0]*10
    temp = N
    prev = 0
    mult = 1
    while temp != prev:
        prev = temp
        while temp != 0:
            Seen[temp%10] = True
            temp = temp//10
        if not 0 in Seen:
            return(mult*N)
        else:
            mult = mult + 1
            temp = mult*N
    else:
        return ('INSOMNIA')
read()
