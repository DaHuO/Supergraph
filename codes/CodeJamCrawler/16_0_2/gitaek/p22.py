
finam = 'in21.txt'
fonam = 'out21.txt'
fi = open(finam)
fo = open(fonam, 'w')
T = int(fi.readline())
for t in range(T):
    cakes = fi.readline().strip()
    c = cakes[0]
    flip = 0
    if len(cakes) > 1:
        for n in range(1,len(cakes)):
            if cakes[n] != cakes[n-1]:
                flip +=1
    if (flip%2==0 and c=='-') or (flip%2 != 0 and c == '+'):
        flip +=1
    sol = 'Case #'+str(t+1)+': '+str(flip)
    print sol
    fo.write(sol+'\n')
fi.close()
fo.close()

        
