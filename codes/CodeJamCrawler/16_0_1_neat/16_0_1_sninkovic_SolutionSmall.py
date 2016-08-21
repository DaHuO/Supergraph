from datetime import datetime,date
import random

def getDigits(a):
    rv={}
    while a>0:
        
        rv[a%10]=1
        a=a/10
        #print a
    return rv



T = int(raw_input())
totenter = datetime.time(datetime.today())
enter= datetime.time(datetime.today())
for t in range(0,T):
    N = int(raw_input())
        #n = random.randint(1900000,2000000)
        #N=n
    delta = N
    figs = {}
    if N==0:
        print "Case #"+str(t+1)+": INSOMNIA"
        continue
    #print len(figs.keys())
    #print 
    while len(figs.keys())<10:
        figs.update(getDigits(N))
        N+=delta
        #print N
    exit = datetime.time(datetime.today())
    #print n, " rezultat", N-delta, "time=", datetime.combine(date.today(),exit)-datetime.combine(date.today(),enter)
    print "Case #"+str(t+1)+":",N-delta
 
totexit = datetime.time(datetime.today())
#print datetime.combine(date.today(), totexit) - datetime.combine(date.today(), totenter)

#print getDigits(120).keys()

        
                                                                
                                                                
