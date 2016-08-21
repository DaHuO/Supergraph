import math

#f= open("C-small-attempt0.in", 'r')
output = open("outputCoin.txt", 'w')
#t = f.readline().strip()

t= raw_input()
t = int(t)
case = 1



   
for a0 in xrange(t):
    #inp = f.readline()
    output.write('Case #' + str(case) + ':\n')
    inp = raw_input().strip().split(' ')
    i = 0
    start = '1'
    for a1 in xrange(int(inp[0]) - 2):
        start += '0'
    start += '1' 
    while(i < int(inp[1])):
        divisors = []
        if start[0] == '1' and start[-1] == '1':
            for base in xrange(2,11):
                num = int(start, base)
                divFound = False
                for x in xrange(int(math.sqrt(num))):
                    if divFound:
                        continue
                    if x > 1 and num % x == 0:
                        divisors.append(x)
                        divFound = True  
            if len(divisors) == 9 and len(start) == int(inp[0]):
                output.write(start)
                print start
                for x in divisors:
                    print ' ' + str(x)
                    output.write(' ' + str(x))
                output.write('\n')
                i += 1
        start = str(bin(int(start,2) + int('1',2)))
        start = start[2:]
    case += 1
        
    
#f.close()
output.close()