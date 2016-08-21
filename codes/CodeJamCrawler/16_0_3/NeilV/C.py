import random

def check_prime(n):
    for i in xrange(2,100):
        if n%i == 0:
            return False,i
    return True,0

def check_jamcoin(string):
    divisors = []
    for base in range(2,11):
        n = int(string,base)
        is_prime,divisor = check_prime(n)
        if is_prime:
            return False,[]
        else:
            divisors.append(divisor)
    return True,divisors

def rand_bin_str(length):
    '''string = ""
    for i in range(length):
        string += str(random.randint(0,1))
    return string'''
    n = random.randint(0,2**length-1)
    return str(bin(n)[2:]).zfill(length)
   

LENGTH = 32
required = 500
jamcoin_list = []
divisor_list = []
iters = 0
num_found = 0

while num_found < required:
    test = "1"+rand_bin_str(LENGTH-2)+"1"
    if test in jamcoin_list:
        continue
    #print test
    is_jamcoin,divisors = check_jamcoin(test)
    if is_jamcoin:
        jamcoin_list.append(test)
        divisor_list.append(divisors)
        num_found += 1
    iters += 1
    print iters,num_found

'''n = 3
while num_found < required:
    test = str(bin(n)[2:]).zfill(LENGTH)
    #print test
    is_jamcoin,divisors = check_jamcoin(test)
    if is_jamcoin:
        jamcoin_list.append(test)
        divisor_list.append(divisors)
        num_found += 1 
    n += 2
    iters += 1'''
    
print "%i iterations" %(iters)
out = open("C_out.txt","w")
out.write("Case #1:\n")
for i in range(len(jamcoin_list)):
    print jamcoin_list[i]
    out.write("%s" %jamcoin_list[i])
    for divisor in divisor_list[i]:
        out.write(" %i" %divisor)
    out.write("\n")

    
 