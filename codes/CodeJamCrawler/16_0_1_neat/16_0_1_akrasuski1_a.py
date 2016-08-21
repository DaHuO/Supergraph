n=int(raw_input())

def digits(num):
    digs=[0]*10
    while num>0:
        dig=num%10
        digs[dig]=1
        num/=10
    return digs

for i in xrange(n):
    num=int(raw_input())
    num0=num
    if num==0:
        print "Case #"+str(i+1)+": INSOMNIA"
        continue
    seen=[0]*10
    while True:
        digs=digits(num)
        cnt=0
        for j in range(10):
            seen[j]|=digs[j]
            cnt+=seen[j]
        if cnt==10:
            print "Case #"+str(i+1)+": "+str(num)
            break
        num+=num0
