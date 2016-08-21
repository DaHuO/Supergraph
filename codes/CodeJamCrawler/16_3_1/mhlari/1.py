import string
import numpy as np
file = open('A-small-attempt3.in.txt','r')
file_out = open('out1.txt','w')
file = file.readlines()
n = int(file[0])
for j in range(1,2*n,2):
    N = int(file[j].strip()) 
    pis = file[j+1].strip().split(' ')
    pis = np.array([int(i) for i in pis])
    out = ''
    pop = sum(pis)
    for step in range(pop):
        outl = ''
        for i in range(2):
            p = sum(pis)
            check = (p-1)/2 +1
            choices = np.where((pis>=check) & (pis>0))[0]
            if len(choices)>0:
                ind = choices[0]
                outl+=string.ascii_uppercase[ind]
                pis[ind] -= 1 
            elif np.all(pis == p/N) and p>0:
                ind = 0
                outl+=string.ascii_uppercase[ind]
                pis[ind] -= 1 
                break
            elif sum(pis)>0:
                choices = np.where((pis>0) & (pis==max(pis)))[0]
                ind = choices[0]
                outl+=string.ascii_uppercase[ind]
                pis[ind] -= 1 

        out += outl + ' '
        if sum(pis) == 0:
            break   
    file_out.write('Case #%i: %s\n'%(j/2+1,out[:-1]))
    
    
    
file_out.close()