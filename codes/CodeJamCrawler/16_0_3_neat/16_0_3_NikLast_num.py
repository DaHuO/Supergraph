import math

def getvalue(num,base,length):
    value = 1
    for bit in format(num, '0%db' % (length-2)):
        value *= base
        if bit == '1':
            value += 1
    value *= base
    value += 1

    return value

def getdivisor(num):
    upper = math.sqrt(num)
    divisor = 2
    while divisor <= upper:
        if num % divisor == 0:
            return divisor
        divisor += 1
    return None


def iscoin(value,length):

    divisors = []
    for base in range(2,10+1):
        newvalue = getvalue(value,base,length)
        divisor = getdivisor(newvalue)
        if divisor:
            divisors.append("%d" % divisor)
        else:
        #no divisors for this base
            break;

    else:
        #comleted successfully
        return divisors 

    return None


n = int(raw_input())
for c in range(n):
    length, num = (int(res) for res in raw_input().split())
    count = 0
    print "Case #%d:" % (c+1)
    for x in range(1,2**(length-2)):
        div =  iscoin(x,length)
        if div:
            coinstring = bin(getvalue(x,2,length))[2:]
            coindiv = " ".join(div)
            print "%s %s" % (coinstring, coindiv)
            count += 1
            if count >= num:
                break;


