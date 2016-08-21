import math
import operator
from bases import Bases
bases=Bases()
import math

t=input()
def p(n):
    if n == 2:
        return False
    if n % 2 == 0 or n <= 1:
        return 2

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return divisor
    return False

funname="bases.fromBase";
n,m=map(int,raw_input().split());
tj=0;
print "Case #1:"
for i in range(0,pow(2,n-2)):
    if(tj==m):
        break;
    k='1'+'{0:014b}'.format(i)+'1'
    l=[];
    l1=[]
    l.append(int(k));
    f=1;
    for j in range(2,11):
        tfun=funname+str(j)+'("'+k+'")';
        l1.append(eval(tfun));
        temp=p(eval(tfun))
        if(temp==False):
            f=0;
            break;
        l.append(temp);
    if f==1:
        print " ".join(str(mli) for mli in l);
        tj=tj+1;
