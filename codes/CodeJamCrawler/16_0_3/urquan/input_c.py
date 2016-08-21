import pyprimes

def numtoBase(num, base):
#Compute the number given by digits in base b.
    n = 0
    for d in num:
        n = base * n + d
    return n

def toDigits(n, b):
#Convert a positive number n to its digit representation in base b.
    digits = []
    while n > 0:
        digits.insert(0, n % b)
        n  = n // b
    return digits

def list_to_int(l):
#Convert a list of ints into a single int
    result = 0
    for c in l: 
        result = (result*10)+c
    return result

def simple_div(n):
    #find the non-trivial divisors of n, terminates if more than 1 element
    i = 1
    list = []
    while i <= n and len(list)<=0:
        if n % i == 0 and i != 1 and i != n:
            list.append(i)
        i = i + 1
    return list

def read_file():
    f = open("C-small-attempt0.in", 'r')
    num_case = int(f.readline())

    for n in range(num_case):
        read_in = f.readline().split()
        num_len = int(read_in[0])
        num_jam = int(read_in[1])     
        
        max_num = 1
        for i in range(num_len-1):
            max_num = (max_num*10)+1

        
        min_num = 1
        for i in range(num_len-1):
            min_num = (min_num*10)
        min_num +=1

        int_to_list = lambda num: map(int, str(num)) #changes an int to a list of single digits
        
        jamcoin_dict = {}
        for jamcoin in range(numtoBase(int_to_list(min_num),2),numtoBase(int_to_list(max_num),2)+1):
            flag = False
            jamcoin = list_to_int(toDigits(jamcoin,2))
            if jamcoin % 10 == 0:
                flag = True
            else:
                divisors = []

                for i in xrange(2,11):
                    dec_num_value = numtoBase(int_to_list(jamcoin),i)
                    if pyprimes.is_prime(dec_num_value):
                        flag = True
                        break
                    divisors.append(str(simple_div(dec_num_value)[0]))

            if len(jamcoin_dict) >= num_jam:
                break
            elif not flag:
                jamcoin_dict[jamcoin] = divisors

        print_result(n+1, jamcoin_dict)


def print_result(case, jamcoin_dict):
    print('Case #{}:'.format(case))
    for k, v in jamcoin_dict.iteritems():
        print k, ' '.join(v)

read_file()