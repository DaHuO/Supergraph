import sys
fileinput = sys.stdin

#import StringIO
#fileinput = StringIO.StringIO(inputstr)

T=int(fileinput.readline())
for t in range(T):
    N=int(fileinput.readline())
    ad=set(str(i) for i in range(10))
    CN=N;
    if CN==0:
        print "Case #%s: %s" % (t+1, "INSOMNIA")
        continue;
    while(True):
        ad = ad-set(str(CN))
        if not ad:
            print "Case #%s: %s" % (t+1, CN)
            break;
        CN +=N
