import math

def check_is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return i
    else:
        return -1

fh = open('prob3.txt','w')

testcase_num = int(input())
testcase_idx = 0

while testcase_idx < testcase_num:
    fh.write("Case #"+str(testcase_idx + 1)+':\n')
    line = input().split()
    digit_num = int(line[0])
    set_num   = int(line[1])
    #print(digit_num, set_num)
    jancoin = int("".join(['1','0' * (digit_num -2),'1']),2)
    found_set = 0
    while found_set < set_num:
        divisor_list = list()
        #print(bin(jancoin))
        for i in range(2,11):
            if i == 11:
                i = 1
            interpretation = 0
            #Count Interpretation
            for exp in range(len(bin(jancoin)[2:])):
                interpretation += int(bin(jancoin)[len(bin(jancoin))-1-exp]) * (i ** exp)
            divisor = check_is_prime(interpretation)
            #print(interpretation)
            if divisor != -1:
                #It's not a prime
                #print(i, ":", interpretation, divisor)
                divisor_list.append(divisor)
            else:
                break
        else:
            # All the interpretation are not prime
            found_set += 1
            fh.write(bin(jancoin)[2:])
            #print(bin(jancoin))
            #print(divisor_list)
            i=1
            for divisor in divisor_list:
                i += 1
                interpretation = 0
                for exp in range(len(bin(jancoin)[2:])):
                    interpretation += int(bin(jancoin)[len(bin(jancoin))-1-exp]) * (i ** exp)
                #print(interpretation, divisor, interpretation%divisor)
                fh.write(" "+str(divisor))
            #print(divisor_list)
            fh.write('\n')
        jancoin = jancoin + 2

    testcase_idx += 1
fh.close()
