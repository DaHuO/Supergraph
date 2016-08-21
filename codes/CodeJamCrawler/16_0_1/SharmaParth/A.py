import sys
orig_stdout = sys.stdout
f = file('ou.txt', 'w')
sys.stdout = f

for j in range(input()):
    n = list(raw_input())
    l = []
    l.append(n[0])
    t = ord(n[0])
    for i in range(1,len(n)):
        if ord(n[i]) >= t:
            l.insert(0,n[i])
            t = ord(n[i])

        else :
            l.append(n[i])

    print "Case #%s: %s"%(j+1,"".join(l))
sys.stdout = orig_stdout
f.close()


