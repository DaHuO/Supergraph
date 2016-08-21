import math

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
            break

def dec_to_bin(num):
    result = ''
    quotient = num
    while quotient>0:
        remainder = quotient%2
        quotient = quotient//2
        result = str(remainder) + result
    return(result)


file = open("C-small-attempt0.in", 'r')
outfile = open("coinjamOUT.txt", 'w')
case = int(file.readline())
line = file.readline().split(' ')
length = int(line[0])
limit = int(line[1])
counter = 0
file.close()

num = '1' + '0'*(length-2) + '1'
outfile.write("Case #1:")
outfile.write('\n')
while counter < limit:
    dec = 0
    for i in range(len(num)):
        dec = dec * 2 + int(num[i])
    if counter != 0:
        dec += 2
        num = str(dec_to_bin(dec))
    var = []
    boolean = None
    for base in range(2,11):
        total = 0
        #calculate base interpretation
        for i in range(len(num)):
            total = total * base + int(num[i])
        var.append(total)
        #check prime
        boolean = is_prime(total)
        if boolean == None:
            break
    if boolean == False:
        counter += 1
    
        divisor = []
        for n in var:
            count = 2
            while n % count != 0:
                count += 1
            divisor.append(count)
        outfile.write(str(num) + ' ')
        for index in range(len(divisor)):
            outfile.write(str(divisor[index]))
            if index != len(divisor)-1:
                outfile.write(' ')
        if counter != limit:
            outfile.write('\n')
outfile.close()
