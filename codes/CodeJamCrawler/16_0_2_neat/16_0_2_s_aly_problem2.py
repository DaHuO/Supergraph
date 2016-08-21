tt = {'+':'-','-':'+'}
def pancake(k):
    m=0
    i=0
    finish=False
    while(finish==False):
        if k[0] == '+':
            i=0
            while (i<len(k) and k[i]=='+'):
                k[i]=tt[k[i]]
                if i == len(k)-1:
                    finish=True
                    break
                i=i+1
        else:
            i=len(k)-1
            while (i>=0 and k[i]=='+'):
                i=i-1
            j=0
            while (j<=i):
                k[i],k[j] = tt[k[j]],tt[k[i]]
                j=j+1
                i=i-1
            k.reverse()    
        m=m+1
    return m-1


t = int(input())
for i in range(1,t+1):
    print("Case #{}: {}".format(i,pancake(list(input()))))
