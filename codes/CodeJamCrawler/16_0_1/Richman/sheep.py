def digits(num):
    rem = []
    while num:
        num,tmprem = divmod(num,10)
        rem += [tmprem]
    return rem

def finddigits(inp,finish):
    fac = 1
    while True:
        num = inp * fac
        fac = fac + 1
        for dig in digits(num):
            finish[dig] = 0
        if all([v == 0 for v in finish]):
            return num

l=0
with open('A-large.in','r') as inputs:
    next(inputs)
    for inp in inputs:
        inp= int(inp.rstrip("\n"))
        finish = [1 for i in xrange(10)]
        # Copy input
        if inp == 0:
            output = "INSOMNIA"
        else:
            output = finddigits(inp,finish)
        l = l+1
        print("Case #%i: %s"%(l,output))
