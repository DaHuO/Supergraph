import fractions,itertools,time

def is_prime(num):
    try:
        timenum=time.time()
        loop=long(2)
        while (loop<num) and ((time.time()-timenum)<5):
            if ((num % loop) == 0):
                return False
            loop=long(loop+1)
        return True
    except:
        pass
        #print num

#get input
t=int(raw_input())
for i in range(1,t+1):
    tempin=raw_input()
    tempin=tempin.split(" ")
    n=int(tempin[0])
    #print n
    j=int(tempin[1])
    #print j
    print "Case #1:"
    count=0
    counter=0
    while count<j:
        result=[0]*n
        result[0]=1
        result[n-1]=1
        tempcount=counter
        for pos in range(1,n-1):
             if tempcount>0 and tempcount/(2**((n-1)-pos-1))>0:
                 tempcount=tempcount-((tempcount/(2**((n-1)-pos-1)))*(2**((n-1)-pos-1)))
                 result[pos]=1
        #print result
        #print counter
        x=[0]*9
        for b in range(2,11):
            value=0
            for l in range(0,len(result)):
                #print result[l]
                if result[l]==1:
                    value=(value)+(b**(len(result)-l-1))
                    #print value
            if is_prime(value):
                #print "%d is prime" % value
                break
            else:
                loop=long(2)
                timenum=time.time()
                while loop<value:
                    #print "loop %d" % loop
                    #print "value %d" % value
                    #print ((value/loop)*loop)
                    #if fractions.gcd(value,int(loop))!=1:
                    if value==((value/loop)*loop):
                        x[b-2]=loop
                        #print "loop: %d" % loop
                        break
                    elif (time.time()-timenum)>10:
                        #print "here"
                        break
                    loop=long(loop+1)
            #print "Value %d in base %d" % (value,b)
        else:
            count+=1
            print "%s %d %d %d %d %d %d %d %d %d" % (''.join(map(str,result)),x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8])
        counter+=1
