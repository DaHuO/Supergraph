from collections import Counter
N = input()

for i in range(1,N+1):
    num = input()
    c = range(10)
    if(num == 0):
        print "Case #{0}: INSOMNIA".format(i)
    else:
        t = 1
        while not len(c) == 0:
            p = t*num        
            for j in map(int,str(p)):
                if j in c:
                    c.remove(j)

            if len(c) == 0:
                print "Case #{0}: {1}".format(i,p)
                break
            else:
                t = t+1
                
                
        
