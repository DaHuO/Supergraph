import sys
fileinput = sys.stdin

#import StringIO
#fileinput = StringIO.StringIO(inputstr)

T=int(fileinput.readline().strip())
for t in range(T):
    R=''
    S=fileinput.readline().strip()
    for c in S:
        if R=='' or c>=R[0]:
            R=c+R
        else:
            R=R+c
    print "Case #%s: %s" % (t+1, R)