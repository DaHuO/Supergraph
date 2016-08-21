def flip(l):
    r=[]
    for j in reversed(l):
        r += [not j]
    return r

def neg(l):
    return [not j for j in l]

def fliprec(l):
    if len(l) == 1:
        if l[0]:
            return 0
        elif not l[0]:
            return 1
    elif len(l) == 0:
        return 0
    
    n=len(l) + 1
    for j in range(len(l)):
        if not l[j]:
            n=j
            break
    if n == (len(l) + 1):
        return 0

    m=len(l) + 1
    for j in range(n, len(l)):
        if l[j]:
            m=j
            break
    
    r=l[m:]
    return (fliprec(neg(r)) + 1)



def solve():
    a=input()
    seq=[]
    for j in reversed(list(a)):
        if j == '+':
            seq+=[True]
        elif j== '-':
            seq+=[False]
    return str(fliprec(seq))


T=int(input());

for t in range(1,T+1):
    print ("Case #" + str(t) + ": " + solve())