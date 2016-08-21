import sys

#inp = sys.stdin
inp = open("A-large.in","r")
outp = open("out","w")
#outp = sys.stdout
def read_inp():
    return inp.readline().strip()

T = int(read_inp())

for t in xrange(1,T+1):
    N0 = int(read_inp())
    
    seen = [False]*10
    numbers = set()
    
    sleep = False
    N = N0
    while N not in numbers:
        numbers.add(N)
        q = N
        seen[q%10] = True
        while True:
            q = int(q/10)
            if q == 0:
                break
            seen[q%10] = True
        for s in seen:
            if not s: break
        else:
            sleep =True
            break
        N += N0                    
    
    if not sleep:
        ans = 'INSOMNIA'
    else:
        ans = N
    outp.write("Case #%d: %s\n"%(t,ans))

outp.close()