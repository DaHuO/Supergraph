from string import maketrans   # Required to call maketrans function.

intab = "+-"
outtab = "-+"
trantab = maketrans(intab, outtab)

def count(n):
    p = 0

    while p < len(n) and n[p] == '+':
        p = p + 1

    n = n[p:]

    if(len(n) ==0):
        return 0
        
    if(len(n) == 1 and n == '-'):
        return 1
    else:
        return 1 + count(n[1:].translate(trantab))

T = input()
for i in range(1,T+1):
    n = raw_input()
    n =  n[::-1] # flipping
    print "Case #{0}: {1}".format(i,count(n))
        
    
