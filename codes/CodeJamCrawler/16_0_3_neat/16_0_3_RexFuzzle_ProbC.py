import pickle
primes = pickle.load(open( "primes16.list", "rb" ) )
print primes

def firlas(inp):
    if int(bin(inp)[2])==1 & int(bin(inp)[-1])==1:
        return True
    else:
        return False

def is_prime(n):
    boo = True
    if n in primes:
#         print "in prime list"
        return True
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = long(n**0.5)
    f = 5
    while f <= r:
#         print '\t',f
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True

def is_prime_set(inp):
    sin = bin(inp)[2:]
    isp = False
    for i in range(2,11):
        boo = is_prime(long(sin,i))
        if boo:
            isp=True
            break
    return isp

def find_div(x):
    factorlist=[]
    loop=2
    while loop<=x:
        if x%loop==0:
            x/=loop
            factorlist.append(loop)
            break
        else:
            loop+=1
    return factorlist[0]

def div_set(inp):
    sin = bin(inp)[2:]
    isp = False
    div=[]
    for i in range(2,11):
        div.append(find_div(long(sin,i)))
    return div


def find_coin(n,j):
    i=long(2**(n-2))
    found=[]
    while (len(bin(i)[2:])<=n)&(len(found)<j):
        i=i+1
#         if firlas(i) & (len(bin(i)[2:])==n):
        if (i%2==1) & (len(bin(i)[2:])==n):
#             print i%2==1
            isp = is_prime_set(i)
            if not isp:
                div = div_set(i)
                print bin(i)[2:],i,div
                found.append(bin(i)[2:]+' '+" ".join(map(str, div)))
    return found




filename='C-large'
file_in = open(filename+'.in','r')
file_out = open(filename+'.out','w')
num_sets=int(file_in.readline())
for i in range(num_sets):
    n,j = file_in.readline().split()
    n=int(n)
    j=int(j)
    file_out.writelines('Case #%s:\n'%(i+1))
    found=find_coin(n,j)
    for k in range(j-1):
        file_out.writelines(found[k]+'\n')
    file_out.writelines(found[-1])
file_in.close()
file_out.close()
