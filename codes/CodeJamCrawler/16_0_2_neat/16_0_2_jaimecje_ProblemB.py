import math

input = open('input.in', 'r')
output = open('output.out', 'w')

cases = int(input.readline())
print 'Casos: '+ str(cases)
t = 0
while t < cases:
    nx = input.readline()
    nm = list(nx)
    sw = 0
    
    i = 0
    all_happy = False
    while all_happy == False:
        es = True
        c = -1
        l = len (nm)
        j = 0
        while j < l:
            if nm[j] =='-':
                es = es and False
                c = j
                print 'MENOS'
            else:
                es = es and True
            j = j + 1
        
        if es:
            all_happy = True
        else:
            sw = sw + 1
            k = 0
            while k <= c:
                if nm[k] =='-':
                    nm[k] = '+'
                else:
                    nm[k] = '-'
                k = k + 1
                print nm

	print nm
		
    output.write("Case #"+str(t+1)+": "+str(sw)+"\n")
    
    t = t + 1

output.close()