# Import the file
in_file = 'C-small.in'
Type = 'small' if in_file.count('small') > 0 else 'large' if in_file.count('large') > 0 else 'test'
out_file = 'C-{0}.out'.format(Type)

#with open(in_file,'r') as f:
#    data = f.readlines()
import random

def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        return(True)
    if n == 3:
        return(True)
    if n % 2 == 0:
        return(2)
    if n % 3 == 0:
        return(3)

    i = 5
    w = 2

    while i * i <= n and i < 100:
        if n % i == 0:
            return(i)

        i += w
        w = 6 - w

    return(True)

def BinaryToBase(Number, Base):
    return(int(Number, Base))

N = 32
J = 500
OUT = []
while True:
    j = random.randint(0, 2**(N-2))
    Test = '1' + bin(j)[2:].zfill(N-2) + '1'
    Vec = [str(int(Test, 10))]
    FLAG = True
    for i in range(2,11):
        Val = isprime(int(Test, i))
        if Val == True:
            FLAG = False
            break
        Vec.append(str(Val))
    if FLAG:
        OUT.append(' '.join(Vec))
        print(Vec)
    if len(OUT) == J:
        break
    
            
        
        

with open(out_file,'w') as f:
    f.write('Case #1:\n')
    for i in range(len(OUT)):
        f.write('{1}\n'.format(i+1,OUT[i]))
