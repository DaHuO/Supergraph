import sys
fileinput = sys.stdin

#import StringIO
#fileinput = StringIO.StringIO(inputstr)

T=int(fileinput.readline().strip())
for t in range(T):
        K,C,S=fileinput.readline().strip().split()
        K,C,S = int(K), int(C), int(S)
        sol = range(1,S+1)
        sol = [(i-1)*(K**(C-1))+1 for i in sol]
        Sstr=" ".join([str(i) for i in sol])
        print "Case #%s: %s " % (t+1, Sstr)
