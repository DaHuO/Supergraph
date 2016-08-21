import sys

def cntFlip(cakes):
    c = cakes[0]
    flip = 0
    if len(cakes) > 1:
        for n in range(1,len(cakes)):
            if cakes[n] != cakes[n-1]:
                flip +=1
    if (flip % 2 == 0 and c == '-') or (flip % 2 != 0 and c == '+'):
        flip +=1
    return flip

f = open(sys.argv[1], 'r')
num = f.readline().strip()
for i in xrange(1, int(num)+1):
    cakes = f.readline().strip()
    flip = cntFlip(cakes)
    ans = 'Case #'+str(i)+': '+str(flip)
    print ans
