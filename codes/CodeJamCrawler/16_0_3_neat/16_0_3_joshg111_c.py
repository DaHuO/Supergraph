import fileinput
from math import sqrt; from itertools import count, islice



def get_divisor(x):
    # Stopping checking for divisors when we hit some pre defined maximum. 
    #for i in islice(count(2), 1000000):
    for i in xrange(2, 1000):
        if (x % i) == 0:
            # This is the case it is not a prime. Return the divisor. 
            return i

    # This is a prime. Unable to get divisor. 
    return None


def init(n):
    x = 1
    for i in xrange(n-1):
        x *= 10
        
    return x+1
    

def gen_num(n):
    len_perm = (n - 2)
    perms = 2 ** len_perm
    formatter = '{:0' + str(len_perm) + 'b}'
    for i in xrange(perms):
        s = formatter.format(i)
        s = '1' + s + '1'
        yield s
    
    
def output_jam(s, divisors):
    f.write(s + " ")
    for d in divisors:
        f.write(str(d) + " ")
    
    f.write("\n")
    
    
def gen_jamcoin(n, j):
    jams = 0
    g_i = gen_num(n)
    while jams < j:
        s = g_i.next()
        divisors = []
        found_jam = True
        for b in xrange(2, 11):
            # Check all the bases
            divisor = get_divisor(long(s, b))
            if not divisor:
                found_jam = False
                break
                
            else:
                divisors.append(divisor)
            
        if found_jam:
            output_jam(s, divisors)
            jams += 1
            print "jams = " + str(jams)
    

f = open('workfile_large', 'w')

if __name__ == "__main__":
    
    
    i = 1
    f_i = fileinput.input()
    tests = f_i.next()
    for line in f_i:
        n, j = map(int, line.split(' '))
        f.write("Case #" + str(i) + ":\n")
        gen_jamcoin(n, j)
        i += 1
        
    f.close()
    f_i.close()