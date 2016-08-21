import sys
from math import sqrt
from itertools import count, islice

input_file = sys.argv[1]
output_file = sys.argv[2]

#input_file = 'input.txt'
#output_file = 'output.txt'

in_file = open(input_file)
out_file = open(output_file,'w')

line_counter = 0

def isPrime(n):
    if n < 2: 
        return 0
        #int(sqrt(n)-1)
    for number in islice(count(3), 500):
        if number < 12:
            if not n%number:
                return number
        if number > 11 :
            if number%2 == 0: continue
            if number%3 == 0: continue
            if number%5 == 0: continue
            if number%7 == 0: continue
            if number%11 ==0: continue
            if not n%number:
                return number
    return 0

list_of_prime = []    
out_file.writelines("Case #1:\n")
for line in in_file:
    if line_counter > 0:
        #print line
        x = line.split()
        N = int(x[0])
        J = int(x[1])
        output =""
        coin_interpretation = []
        divisors = []
        isJamCoin = 1
        coin_counter = 0
        seq = 0
        while True:
            seq+=1
            coin = "1{}1".format("{0:b}".format(seq).zfill(N-2))
            #print "coin: {}".format(coin)
            isJamCoin = 1
            coin_interpretation=[]
            coin_divisors=[]
            output=""
            #print '------------------------------------------------------'
            
        #     coin ='111111 '
            for i in xrange(2,11):
                interpret = int(coin,i)
                #print "interpret: {}".format(interpret)
                p = isPrime(interpret)
                if p > 0:
                    coin_interpretation.append(interpret)
                    coin_divisors.append(p)
                    #print "p: {}".format(p)
                else:
                    isJamCoin = 0
                    break
        
            #print "isJamCoint: {}".format(isJamCoin)        
            if isJamCoin == 1:
                #print coin_interpretation
                coin_counter += 1
                for n in coin_divisors:
                    output = output + str(n) +" "

                print "[{}]{} {}".format(coin_counter,coin,output)
                out_file.writelines("{} {}\n".format(coin,output))
                divisors = []
        #     print "coin_counter: {}".format(coin_counter)
            if coin_counter == J:
                break
        #     print "{}".format(coin)


    line_counter+=1
in_file.close()