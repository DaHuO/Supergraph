import sys
orig_stdout = sys.stdout
f = file('ou.txt', 'w')
sys.stdout = f

for i in range(input()):
    n = int(raw_input())
    if n == 0:
        print "Case #%s: INSOMNIA"%(i+1)
    else :
        j = 1
        l = set()
        lis = []
        while True:
            temp = set(str(n*j))

            if len(l) == 10:
                print "Case #%s: %s"%(i+1, lis[-1])
                break
            else :

                l = l|temp
                lis += [n*j]
                j += 1
sys.stdout = orig_stdout
f.close()