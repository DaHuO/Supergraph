f=open('A-small-attempt0.in.txt', 'r')
r=open('result.txt', 'w')

s2=set([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

def setting(num):
    tmp=[]
    for i in range(1, 100):
        temp=num*i
        print temp
        while temp>0:
            tmp.append(temp%10)
            temp/=10
            print temp
        res=set(sorted(tmp))
        print res, tmp
        if s2==res:
            return num*i

    return -1

l=int(f.readline())
for i in range(1,1+l):
    tmp=int(f.readline())
    key=setting(tmp)
    if key!=-1:
        r.write('Case #'+str(i)+': '+str(key)+'\n')
    else:
        r.write('Case #'+str(i)+': INSOMNIA\n')


