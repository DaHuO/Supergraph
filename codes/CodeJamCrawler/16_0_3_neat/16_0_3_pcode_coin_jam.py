import itertools
import math
prime_cache = {}
def coin_jam(N, J):
    total = []
    for bin_string in itertools.product("01", repeat=N):
        #print "binstring", bin_string
        if bin_string[0] != '1' or bin_string[-1] != '1':
            continue
        divisor_list = []
        invalid = False
        for base in xrange(2, 11):
            #print "base",base
            value = 0
            position = len(bin_string) - 1
            for char in bin_string:
                value += int(char) * (base ** position)
                position -= 1
            divisor = prime_check(value)
            if divisor is not None:
                #print "found divisor", divisor
                divisor_list.append(str(divisor))
            else:
                invalid = True
                break
        if invalid:
            continue
        else:
            total.append("%s %s" %(''.join(bin_string), ' '.join(divisor_list)))
            if len(total) == J:
                return total

def prime_check(value):
    #print "value", value
    if value in prime_cache:
        return prime_cache[value]
    for num in xrange(2, int(math.sqrt(value))):
        if value % num == 0:
            prime_cache[value] = num
            return num
    return None
    
T = int(raw_input())
solutions=[]
for case in xrange(T):
    N,J = map(int, raw_input().split())
    sol = coin_jam(N, J)
    solutions.append('Case #'+str(case+1)+':')
    solutions.extend(sol)

#for solution in solutions:
#    print solution

with open('coin_jam_out.txt', 'w') as f:
    for s in solutions[:-1]:
        f.write(s)
        f.write("\n")
    f.write(solutions[-1])