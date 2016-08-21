
inF = open('A-large.in.txt','r')
ouF = open('MaryamQAL.out','w')
t = int(inF.readline())
for x in xrange(t):
    n = int(inF.readline())
    comp = set([0,1,2,3,4,5,6,7,8,9])
    dig = set(map(int, str(n)))
    i = 2
    if n == 0 :
        ouF.write("Case #" + str(x+1) + ': INSOMNIA\n')
    else:
        while comp != dig :
            s = n*i
            dig = dig.union(set(map(int, str(s))))
            i += 1
        ouF.write("Case #" + str(x+1) + ': '+str((i-1)*n) +'\n')
             
       
inF.close()
ouF.close()
 

