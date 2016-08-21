import numpy as np
import itertools

def smallest_divisor(n):
    divisor=0
    x=2
    while x<=np.sqrt(n):
        if n%x==0:
            divisor=x
            break
        x+=1
    return divisor
        

def generate_jamcoins(N,J):
    fout=open('jamcoins_'+str(N)+'_'+str(J)+'.out','w')
    fout.write('Case #1:\n')
    jc_generator=itertools.product('01',repeat=N-2)
    powers=range(N-1,-1,-1)
    n=0
    while n<J:
        jamcoin=['1']+list(jc_generator.next())+['1']
        divisors=[]
        for base in [2,3,4,5,6,7,8,9,10]:
            x=0
            for i in range(len(powers)):
                x+=base**powers[i]*int(jamcoin[i])
            divisor=smallest_divisor(x)
            if divisor==0:
                break
            else:
                divisors.append(divisor)
        if len(divisors)==9:
            print jamcoin
            n+=1
            for bit in jamcoin:
                fout.write(bit)
            for divisor in divisors:
                fout.write(' '+str(divisor))
            fout.write('\n')
    fout.close()
            
        
    