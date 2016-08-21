import numpy as np

def ambi_sieve(n):
    s = np.arange(3, n, 2)
    for m in range(3, int(n ** 0.5)+1, 2):
        if s[(m-3)/2]:
            s[(m*m-3)/2::m]=0
    return np.r_[2, s[s>0]]

filename = "C-test"
infile = filename+ ".in"
outfile = filename+ ".out"

f_in = open(infile, 'r')
f_out = open(outfile, 'w')

f_in.readline()
line = f_in.readline().strip()
N = int(line.split()[0])
J = int(line.split()[1])
print(N,J)

f_out.write("Case #1: \n")
limit = 100000
primes = ambi_sieve(limit)


count = 0
for basenum in range(2**(N-1)+1,2**N,2):
    binstr = bin(basenum)[2:]
    bases = []
    good = False
    for b in range(2,11):
        good = False
        num = int(binstr,b)
        for p in primes:
            if num % p == 0 and num != p:
                bases.append(p)
                good = True
                break;
        if not good:
            break;
    if len(bases) == 9:
        print(binstr + " " + ' '.join(map(lambda x:str(int(x)),bases)))
        f_out.write(binstr + " " + ' '.join(map(lambda x:str(int(x)),bases)) + "\n")
        count += 1
        if count == J:
            break;

