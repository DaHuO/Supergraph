
def isHappy(ls):
    ts = filter(lambda x:x==0,ls)
    if len(ts)==0:
        return 1
    else:
        return 0

def flip(ls,n):
    for i in range(0,n):
        if(ls[i]==0):
            ls[i]=1
        elif(ls[i]==1):
            ls[i]=0
    return ls

def getFlipped(ls):
    count = 0
    if(isHappy(ls)==1):
        return count;
    for i in range(0,len(ls)-1):
        if(ls[i]!=ls[i+1]):
            ls = flip(ls,i+1);
            count += 1
            if(isHappy(ls)==1):
                #print ls
                return count
    ls = flip(ls,len(ls))
    count += 1
    #print ls
    return count



t = input()
ps = []

for i in xrange(t):
    xs = []
    inps = raw_input();
    for i in inps:
        if i=='-':
            xs.append(0)
        else:
            xs.append(1)
    ps.append(xs)

cnt = 1
for i in xrange(t):
    ans =  getFlipped(ps[i])
    print "case #"+str(cnt)+": ",ans
    cnt += 1
