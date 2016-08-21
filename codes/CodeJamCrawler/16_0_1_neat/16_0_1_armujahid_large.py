
def getOutput(N):
    if N == 0:
        return "INSOMNIA"
    digitToBeSeen = ['0','1','2','3','4','5','6','7','8','9']
    ans = N
    multipliar = 2
    while True:
        removeDigits(digitToBeSeen,ans)
        if len(digitToBeSeen) == 0:
            return ans
        ans = N *multipliar
        multipliar = multipliar+1

def removeDigits(digitToBeSeen,ans):
    strAns = str(ans)
    for c in strAns:
        try:
            digitToBeSeen.remove(c)
        except ValueError:
            pass
    
T = int(input())  # read a line with a single integer
for i in range(1, T + 1):
    N = long(input()) 
    output = getOutput(N)
    print "Case #{}: {}".format(i, output)


