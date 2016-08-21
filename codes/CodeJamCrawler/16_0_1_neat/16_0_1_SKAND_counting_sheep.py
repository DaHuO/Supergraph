a = input()
b=[]
c=[]

for i in range(a):
    b.append(input())
    c.append('Case #'+str(i+1)+':')


def func(num):
    d={}
    for j in range(1,10**2+1):
        k = str(j*num)
        for l in range(len(k)):
            d[k[l]] = 1
            if len(d) == 10:
                return (j*num)
            if j == 10**2 or num == 0:
                return 'INSOMNIA'

for asd in range(a):
    print c[asd], func(b[asd])
