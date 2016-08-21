f = open("A-small-attempt0.in.txt",'r')
A = open("output.txt",'w')

C = f.readline()
for c in xrange(0,int(C)):
    d = {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 0:False}
    N = int(f.readline())
    if N is 0:
        answer = 'Case #{0}: INSOMNIA'.format(c+1)
        print answer
        A.write(answer+'\n')

    else:
        i = 1
        while(False in d.values()):
            n = i*N
            td = [int(k) for k in str(n)]
            for l in td:
                d[l] = True
            i+=1
        answer = 'Case #{0}: {1}'.format(c+1,n)
        print answer
        A.write(answer+'\n')
f.close
A.close
