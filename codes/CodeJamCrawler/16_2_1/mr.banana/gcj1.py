def delete(x,l):
    for i in ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"][x]:
        l.remove(i)
    return l
t=int(input())
for case in range(1,t+1):
    s=sorted(list(input()))
    l=[]
    while 'Z' in s:
        l.append(0)
        s=delete(0,s)
    while 'G' in s:
        l.append(8)
        s=delete(8,s)
    while 'X' in s:
        l.append(6)
        s=delete(6,s)
    while 'W' in s:
        l.append(2)
        s=delete(2,s)
    while 'S' in s:
        l.append(7)
        s=delete(7,s)
    while 'T' in s:
        l.append(3)
        s=delete(3,s)
    while 'Z' in s:
        l.append(0)
        s=delete(0,s)
    while 'V' in s:
        l.append(5)
        s=delete(5,s)
    while 'F' in s:
        l.append(4)
        s=delete(4,s)
    while 'O' in s:
        l.append(1)
        s=delete(1,s)
    while 'N' in s:
        l.append(9)
        s=delete(9,s)
    print('Case #%s: '%(case)+''.join(sorted([str(i) for i in l])))
    
    
