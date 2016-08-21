import itertools
import math

def get_binary(N):
    return ("".join(seq) for seq in itertools.product("01", repeat=N))

def to_base_x(binary, x):
    bin_str = str(binary)[::-1]
    res = 0
    for i in range(len(bin_str)):
        bit = bin_str[i]
        if bit == '1':
            res += pow(x,i)
    return res

def find_divisor(n):
    for i in range(3, 2000):
        if n%i == 0:
            return i
    return -1


def find_binary(N,J):
    ret_dict = {}
    g = get_binary(N-2)
    while len(ret_dict.keys())<J:
        binary = next(g)
        binary =  '1'+binary+'1'
        prime = False
        divisors = []
        for i in range(2,11):
            decimal = to_base_x(int(binary),i)
            d = find_divisor(decimal)
            if d == -1:
                prime = True 
                break
            else:
                divisors.append(str(d))
        if not prime:
            ret_dict[binary]=divisors
        if len(ret_dict.keys()) == J:
            return ret_dict
    return ret_dict

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    N, J = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    print "Case #{}: ".format(i)
    solution = find_binary(N,J)
    for key in solution:
        values = solution[key]
        value = ' '.join(values)
        print str(key) +' '+ value

