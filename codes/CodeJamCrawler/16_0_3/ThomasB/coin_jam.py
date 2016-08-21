def save_answers(location,jamcoins):
    fout = open(location,'w')
    fout.write('Case #1:\n')
    for jamcoin in jamcoins:
        fout.write(jamcoin[0]+' '+' '.join([str(v) for v in jamcoin[1:]])+'\n')
    fout.close()
    
import math
def check_prime(n):
    ''' Return 0 if it is prime, and a divisor if not '''
    for i in range(2,int(math.sqrt(n))):
        if n % i == 0:
            return i
    return 0

def convert_to_base(s,b):
    ''' Return integer of string s, in base b '''
    return int(s,b)
    
def convert_int_to_bin(n,N):
    ''' Convert n into a binary representation, of length N '''
    s = bin(n)[2:]
    s = ''.join(['0' for i in range(0,N-len(s))]) + s
    return s
    
def check_if_jamcoin(s):
    ''' Return False if not a jamcoin, else a list of divisors '''
    divisors = []
    for b in [2,3,4,5,6,7,8,9,10]:
        n = convert_to_base(s,b)
        divisor = check_prime(n)
        if divisor == 0:
            return False
        else:
            divisors.append(divisor)
    return divisors

def generate_jamcoins(N,J):
    ''' Generate J jamcoins of length N. First digit is 1, last digit is 1 (so increments of 2) '''
    jamcoins = [] # list of: [binary,div2,div3,..,div10]
    n = 2**(N-1) + 1
    while J > 0:
        s = convert_int_to_bin(n,N)
        print 'Trying %s.' % s
        divisors = check_if_jamcoin(s)
        if divisors:
            J -= 1
            jamcoins.append([s]+divisors)
            print 'Found one! %s to go.' % J
        n += 2
    return jamcoins

N, J = 16, 50
location_out = 'output_small.txt'

jamcoins = generate_jamcoins(N,J)

save_answers(location_out,jamcoins)
