def nextdigits(n,i=1,digits=None):
    if n==0:
        return "INSOMNIA"
    ni=n*i
    if not digits:
        digits=set()
    digits |= set(str(ni))
    if len(digits)==10:
        return ni
    else:
        return nextdigits(n,i+1,digits)
with open(r"/home/dta/Downloads/jam/input.txt",mode='r') as f1:
    finput=f1.readlines()
T=int(finput[0])
with open(r"/home/dta/Downloads/jam/output.txt",mode='w') as f2:
    for x in range(1,T+1):
        N=int(finput[x])
        y=nextdigits(N)
        f2.write("Case #{x}: {y}\n".format(x=x,y=y))


