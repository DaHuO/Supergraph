import sys

def filled(A):
    for i in A:
        if i==0:
            return False
    return True


def computeLastNum(n,i,A):
    if n==0:
        return "INSOMNIA"
    x = n*i
    num = n*i
    while x > 0:
        A[x%10]=1
        x/=10
    if(not filled(A)):
        return computeLastNum(n,i+1,A)
    return num

if __name__ == "__main__":
    f = open(sys.argv[1],'r')
    N = int(f.readline())
    for i in xrange(1,N+1):
        A=[0,0,0,0,0,0,0,0,0,0]
        n = int(f.readline())
        out = computeLastNum(n,1,A)
        print "Case #" + str(i) + ": " + str(out)
    f.close()
    
