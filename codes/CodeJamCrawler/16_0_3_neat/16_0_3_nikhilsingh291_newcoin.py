from math import sqrt
import itertools
def mrange(start, stop, step):
    while start < stop:
        yield start
        start += step



def is_prime(num):
    if num == 2:
        return True
    if (num < 2) or (num % 2 == 0):
        return False
    return all(num % i for i in mrange(3, int(sqrt(num)) + 1, 2))


def div(x):
    for j in range(2,num):
        if (num%j==0):
            ans.append(j)
    



c=0
print("Case #1:")
for st in itertools.product('01', repeat=14):
    
    st2=''.join(str(x) for x in st)
    st1=list(st2)
    st1.insert(0,1)
    st1.insert(15,1)
    st3=''.join(str(y) for y in st1)
    #print st1,st2
    ans=[st3]
    for i in range(2,11):
        num=int(st3,i)
        if(is_prime(num)==False):
            ans.append(num)
    
        
    if (len(ans)==10):
        c=c+1
        
        ab=[]
        for k in range(1,10):
            for l in range (2,1000000):
                if (ans[k]%l==0):
                    ab.append(l)
                    break
        if(c<=50):
            print long(ans[0]),ab[0],ab[1],ab[2],ab[3],ab[4],ab[5],ab[6],ab[7],ab[8]
        else:
            break
        
