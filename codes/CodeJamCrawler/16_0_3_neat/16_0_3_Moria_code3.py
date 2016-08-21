from math import sqrt
global c
def mrange(start, stop, step):
    while start < stop:
        yield start
        start += step
def factors(n):
    print 'infactors'
    result = set()
    for i in mrange(2, 20001,1):
        div, mod = divmod(n, i)
        if mod == 0:
            result= min(i,div)
            break
    if i==20000:
        result=-1
    return result
from math import sqrt

def is_prime(num):
    print 'inprime'
    if num == 2:
        return True
    if (num < 2) or (num % 2 == 0):
        return False
    return all(num % i for i in mrange(3, int(sqrt(num)) + 1, 2))
def convert(s,base):
    global c
    s1=map(int,list(s))
    b=map(lambda p: base**(len(s)-1-p),range(len(s)))
    c=reduce(lambda a,b:a+b,map(lambda a,b: a*b,s1,b))
    return is_prime(c)
f=open('C-large.in','r')
nt=int(f.readline().strip())
tn=f.readline().strip().split(' ')
f.close()
tnint=map(int,tn)
ln=tnint[0]
g=open('outputbig.txt','w')
g.write('Case #1:')
g.write('\n')
#ln=16
maxi=0
for i in xrange(2**(ln-2)):
    m='1'+bin(i)[2:].zfill(ln-2)+'1'
    lp=[]
    count=0
    l=[]
    for i in range(2,11):
        if convert(m,i):
            count=1
            break
        else:
            if factors(c)==-1:
                count=1
            else:
                lp.append(factors(c))
    if count==0:
        print '{0} : {1} : {2}'.format(maxi+1,m,lp)
        g.write(m)
        g.write(' ')
        for ele in lp:
            g.write(str(ele))
            g.write(' ')
        g.write('\n')
        maxi=maxi+1
    if maxi >= tnint[1]:
        break

g.close()