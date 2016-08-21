import math

input_file = open("C-small-attempt0.in",'r')
output_file = open("C-small-attempt0.out",'w')
#T = int(raw_input())
T = int(input_file.readline())
nontrivial = []

def check_coinjam(n):
    for i in xrange(2,11):
        if(is_prime(int(n,i))):
            return 0
    return 1

def is_prime(num):
    global nontrivial
    for i in xrange(2,int(math.ceil(math.sqrt(num)))):
        if(num % i == 0):
            nontrivial.append(i)
            return 0
    return 1

for i in xrange(0,T):
    #N,J = map(int, raw_input().split(' '))
    N,J = map(int, input_file.readline().split(' '))
    count = 0

    output_file.write('Case #' + str(i+1) + ':\n')
    #print 'Case #' + str(i+1) + ':'
    max_num = 0
    for k in xrange(0,N-2):
        max_num += pow(2,k)
    for k in xrange(0,max_num+1):
        input_str = []
        nontrivial = []
        input_str.append('1')
        bin_str = bin(k)
        bin_str = bin_str[2:len(bin_str)]
        for l in xrange(0,N-2-len(bin_str)):
            input_str.append('0')
        for l in xrange(0,len(bin_str)):
            input_str.append(bin_str[l])
        input_str.append('1')
        input_num = "".join(input_str)
        if(check_coinjam(input_num)):
            count += 1
            output_file.write(input_num + ' ')
            #print input_num + ' ',
            for l in xrange(0,8):
                output_file.write(str(nontrivial[l]) + ' ')
                #print str(nontrivial[l]) + ' ',
            output_file.write(str(nontrivial[8]) + '\n')
            #print str(nontrivial[8])
        if(count == J):
            break

input_file.close()
output_file.close()
