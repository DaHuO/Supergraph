list_digits=[]
def find_digits(num):
    digits=[]
    while num>0:
        rem=num%10
        digits.append(rem)
        num=num/10
    return digits
def check(N,i,NUM,d=''):
    d=find_digits(N)
    for di in d:
        list_digits.append(di)
    #print 'digits are ',list_digits
    base=[1,2,3,4,5,6,7,8,9,0]
    val=False
    for v in base:
        if v not in list_digits:
            val=False
            break
        else:
            val=True
    #print val
    if val:
        #print 'val is true'
        return N
    elif NUM == 0:
        #print 'modulo'
        return None
    else:
        N=i*NUM
        i=i+1
        return check(N,i,NUM)
T=int(input())
for i in range(0,T):
    x=int(input())    
    res=check(x,2,x)
    #print res    
    if res!=None:
        print 'Case #%d: %d' % (i+1,res)
    else:
        print 'Case #%d:'%(i+1),'INSOMNIA'
    list_digits=[]
    
    

