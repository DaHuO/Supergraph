#!/usr/bin/python

fp = open('numeros.txt')
qt = int(fp.readline())
case = 0
for line in fp.readlines():
    case += 1
    if case > qt:
       break
    n = int(line)
    if n == 0:
        print 'Case #{}: INSOMNIA'.format(case)
	continue
    res = [False,False,False,False,False,False,False,False,False,False]
    i = 1
    while True:
	calc = i*n
        # print '{}={}'.format(i, calc),
	for num in str(calc):
	    res[int(num)] = True
	if all(res):
            print 'Case #{}: {}\n'.format(case, calc),
	    break
        i+=1
