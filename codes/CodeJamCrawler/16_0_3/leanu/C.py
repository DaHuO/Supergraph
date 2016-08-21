# initial set of primes, little optimiation:
sprimes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,47,53,59,61,67,71,73,79,83,89,97,101]

def is_prime(n):
    # optimistic way
    global sprimes
    for k in sprimes:
        if k>n**0.5:
            return -1 # wasn't divided by any prime
        if n%k==0:
            return k
    return -1

def str_to_base(s, b):
    #maxpower:
    p = len(s)-1
    n = 0
    for i in range(0,len(s)):
        n += int(s[i]) * b **(p-i)
    return n
    
def num_to_str(n):
    return str(bin(n))[2:]  
         
def get_divisors(s): #string as input
    divisors = []
    for k in range(2, 11):
        d = is_prime(str_to_base(s, k))
        if d==-1:
            return []
        divisors.append(d)
    return divisors

def run(N, J):
    f = open('output.txt','w')
    f.write('Case #1:\n')
    # intial number -1 for loop:
    c = 2**(N-1) - 1
    i=0
    while i<J:
        c = c+2 # increment binary number by 10, as lsb is always 1
        s = num_to_str(c) # get binary representation as str
        d = get_divisors(s)
        if len(d)==0:
            continue
        f.write('%s %s %s %s %s %s %s %s %s %s\n' % (s, d[0], d[1], d[2], d[3], d[4], d[5], d[6], d[7], d[8]))
        i+=1
    f.close()

f = open('input.in', 'r')
T = int(f.readline())
N, J = f.readline().split(' ')
N = int(N)
J = int(J) # na vseakii sluchai

run(N, J)
