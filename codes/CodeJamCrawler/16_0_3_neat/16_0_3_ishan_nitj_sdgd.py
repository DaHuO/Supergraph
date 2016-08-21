import sys
def go1():
    n=0
    n=n|(1<<0)
    n=n|(1<<15)
    n=n|(1<<16)
    n=n|(1<<31) 
    sum=0
    for i in range(1,15):
        for j in range(i+1,15):
            for k in range(j+1,15):
                for l in range(k+1,15):
                     x=n
                     x=x|(1<<i)
                     x=x|(1<<j)
                     x=x|(1<<k)
                     x=x|(1<<l)
                     x=x|(1<<(i+16))
                     x=x|(1<<(j+16))
                     x=x|(1<<(k+16))
                     x=x|(1<<(l+16))
                     sys.stdout.write('{0:32b}'.format(x))
                     sys.stdout.write(' ')
                     for idx in range(2,11):
                         ans=idx**0+idx**15+idx**i+idx**j+idx**k+idx**l
                         sys.stdout.write(str(ans))
                         sys.stdout.write(' ')
                     sys.stdout.write('\n')
                     sum+=1
                     if sum==500:
                         break
                if sum==500:
                    break
            if sum==500:
                break
        if sum==500:
            break 
    
    
print('Case #1:')
go1()
            
