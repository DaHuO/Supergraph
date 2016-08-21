a = input()
b=[]
c=[]

for i in range(a):
    b.append(raw_input())
    c.append('Case #'+str(i+1)+':')


def func(odr):
    i=0
    j=0
    k=1
    if odr[-1] == '+':
        k = 0
    while i < len(odr):
        if len(odr) == i+1:
            i += 1
            continue
        m = odr[i]
        n = odr[i+1]
        i += 1
        if m != n:
            j += 1

    return j + k

for asd in range(a):
    print c[asd], func(b[asd])
