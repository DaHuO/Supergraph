#!/usr/bin/python2.7

for case in range(input()):
    N = input()
    sol = 0
    if (N == 0):
    	print 'Case #%s: INSOMNIA' % (case + 1)
    else:
        i = 1
        lista = [0]*10
        while (sol == 0):
            t = i*N
            while True:
                lista[(t%10)] = 1
                t = t//10
                if (t == 0):
                    break
            if (sum(lista)==10):
                sol = i*N
#            print i*N, lista
            i+=1

    	print 'Case #%s: %s' % ((case + 1), str(sol))

