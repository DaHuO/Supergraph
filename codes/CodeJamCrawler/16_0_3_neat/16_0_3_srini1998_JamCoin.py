from random import randint
import math

def to_decimal(num, base):
    #print num, base
    if ((base == 10) or (num == 0)):
        return num
    else:
        i = 0
        dec = 0
        while (num > 0):
            digit = num % 10
            num //= 10
            if (digit == 1):
                dec += base ** i 
            i += 1
        #print "in decimal is", dec   
        return int(dec)
                
def gimme_a_num(length):
    num = "1"
    for i in xrange(1, length-1):
        num += str(randint(0,1))
    num += "1"
    return int(num)

def get_divisor(num):
    #print ("getting divisor for", num)
    divisor = 0
    if (num % 2 == 0):
        divisor = 2
    else:
        #for i in xrange(3, int(math.sqrt(num))+1,2):
        for i in xrange(3,min(int(math.sqrt(num))+1,1000),2):
            #print "i =", i
            if get_divisor(i) != 0:
                pass
            else:
                if (num % i == 0):
                    divisor = i
                    break
    #print "divisor=", divisor                
    return divisor

t = int(raw_input())  # number of cases
for i in xrange(1, t + 1):
    length, number = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    
#print to_decimal(100,10)
#print gimme_a_num(5)
#print get_divisor(111001)
result = []
numbers = set()
while len(result)<number:
    num = gimme_a_num(length)
    if num not in numbers:
        numbers.add(num)
        #print "num", num
        num_and_divisors = [num]
        for i in xrange(2,11):
            divisor = get_divisor(to_decimal(num, i))
            if  divisor == 0:
                #print "failed for", num, "on base", i
                break
            else:
                num_and_divisors.append(divisor)
        #print "number + divisor length", len(num_and_divisors)
        if len(num_and_divisors) == 10:
            #print "success; appending", num_and_divisors
            result.append(num_and_divisors)
print "Case #1:"
for lst in result:
    #print "list is ", lst
    out = ""
    for j in lst:
        out += str(j)+' '
    print out
   

