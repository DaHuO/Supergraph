import os
import sys

base_map = {2: [pow(2,x) for x in range(0,32)],
            3: [pow(3,x) for x in range(0,32)],
            4: [pow(4,x) for x in range(0,32)],
            5: [pow(5,x) for x in range(0,32)],
            6: [pow(6,x) for x in range(0,32)],
            7: [pow(7,x) for x in range(0,32)],
            8: [pow(8,x) for x in range(0,32)],
            9: [pow(9,x) for x in range(0,32)],
            10: [pow(10,x) for x in range(0,32)]}

def get_base_num_from_binary(b_num,base):
    res = 0
    length = len(b_num)
    for i in range(0, length):
        if b_num[length-i-1] == '1':
             res = res + base_map[base][i]
    return res

def check_prime(num):
    if num <= 3:
        return -1
    if num % 2 == 0:
        return 2
    if num % 3 == 0:
        return 3
    i = 5
    while i*i <= num:
        if num % i == 0:
            return i
        if num % (i + 2) == 0:
            return i+2
        i = i + 6
    return -1 

def make_binary_from_dec(num):
    bin = []
    while num > 0:
        r = num % 2
        bin.insert(0,str(r))
        num = num / 2
    return "".join(bin)

def check_all_bases(num, op):
    binary = make_binary_from_dec(num)
    if binary[-1:] == '0':
        return
    divisors = []
    for i in range(2,11):
        num_base = get_base_num_from_binary(binary, i)
        res = check_prime(num_base)
        if res == -1:
            return False
        divisors.append(str(res))
    op.write("%s %s\n" % (binary, " ".join(divisors)))
    return True

def compute_numbers(N, J, op):
    coinjams_found = 0
    start_bin = "1%s1" % ("0"*(N-2))
    end_bin = "%s" % ("1"*N)
    start_dec = get_base_num_from_binary(start_bin, 2)
    end_dec = get_base_num_from_binary(end_bin, 2)
    for num in range(start_dec, end_dec+1):
        res = check_all_bases(num, op)
        if res == True:
            coinjams_found = coinjams_found + 1
            if coinjams_found == J:
                return    

def coin_jam(inp):
    op = open("output.txt","w")
    ip = open(inp)
    file_inp = ip.read().splitlines()
    test_cases = int(file_inp[0])
    for case in range(1,test_cases+1):
        op.write("Case #%s:\n" % case)
        length, count = file_inp[case].split(" ")
        compute_numbers(int(length), int(count), op)

    op.close()
    ip.close()


if __name__ == '__main__':
    coin_jam(sys.argv[1])

