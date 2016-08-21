t = int(input())  
N, J = [int(x) for x in input().split(' ')]


def print_result(test):
    print("Case #{}:".format(test))
    

from math import sqrt
from itertools import count, islice

def isPrime(n):
    if n < 2: return False
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    for number in islice(count(3,2), int(sqrt(n)-1)):
        if not n%number:
            return False
    return True        

def non_trivial_divisor(n):
    for number in islice(count(2), int(sqrt(n))):
        if n%number == 0:
            return number
    return 1

def convert_base(num,base):
    res = 0
    k = len(num)-1
    for i in num:
        res += int(i)*pow(base,k)
        k -= 1
    return res
    
# print(test_stacks)
def int2bin(i,length_need):

    s = "{0:b}".format(i)
        
    if len(s) < length_need:
        temp = ''.join(['0' for _ in range(length_need-len(s))])
        return temp+s
    else:
        return s[len(s)-length_need:]
    
def is_not_prime_210bases(num):
    
    for i in range(2,11):
        base_num = convert_base(num,i)
        if isPrime(base_num):
            return False
            
    return True
         
jam_coin_list = []
legitimate_jamcoins = []

def find_jamcoin():
    count = 0
    for i in range(0,pow(2,N-2)):
        num_check = '1' + int2bin(i,N-2) + '1'
        # print(num_check)
        # print("{} {}".format(num_check,convert_base(num_check,2)))
        if is_not_prime_210bases(num_check):
            # print("{} {}".format(num_check,convert_base(num_check,2)))
            # jam_coin_list.append(num_check)
            if check_legitimate(num_check):
                count += 1
        if len(legitimate_jamcoins) == J:
            break
            
def check_legitimate(jamcoin):
    temp_base_div = []
        # print(jamcoin)
    for i in range(2,11):
        base_num = convert_base(jamcoin,i)
        temp_divisor = non_trivial_divisor(base_num)
            # print(temp_divisor)
        if (temp_divisor != 1) and (temp_divisor != base_num) :
            temp_base_div.append(temp_divisor)
        else:
            break
    if  len(temp_base_div) == 9:
        legitimate_jamcoins.append([jamcoin,temp_base_div])
        return True
                
    # print(legitimate_jamcoins)    
        # if len(jam_coin_list) == J:
        #     break

find_jamcoin() 
# check_legitimate()


for k in range(t):
    print_result(k+1)
    for i in range(J):
        s = ''
        s += legitimate_jamcoins[i][0]
        for j in legitimate_jamcoins[i][1]:
            s += ' '+str(j)
        #     s.join(' ')
        #     s.join(str(j))
        print(s)