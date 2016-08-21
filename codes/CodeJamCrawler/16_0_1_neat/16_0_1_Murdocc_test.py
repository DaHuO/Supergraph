import sys
def check(b):
    global m
    i=2
    for k in str(b):
        m[i]=1
    prev=-1
    a=b
    while(a<sys.maxint and a!=prev):
       prev=a
       a=i*b
       i=i+1
       count=0
       temp=str(a)
       for alpha in temp:
           m[alpha]=1
       for alpha in '0123456789':
           count=count+m[alpha]
       if(count==10):
            return a
    return 'INSOMNIA'
        
        

n=int(raw_input())
m=dict()
for i in range(10):
    m[str(i)]=0
test=0
for i in range(n):
    input=int(raw_input())
    test+=1
    print 'Case #'+str(test)+':'+' '+str(check(input))
    for i in range(10):
        m[str(i)]=0