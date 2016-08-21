import math


def toInt(n, base):
    return (int(str(n), base))

def toBinary(n):
    return str(bin(n))[2:]

def get_divisor(n):
    for i in range(3,int(math.sqrt(n)+2),2):
        if (n%i == 0):
            return i
    return 0

def process(n):
    coin = 0
    end = 2**n
    n = 2**(n-1) + 1
    count = 0
    while (coin < end):
        divisors = []
        div = 0 
        n = toBinary(n)
        #print(n)
        for i in range(2, 11):
            #print(toInt(n, i))
            div = get_divisor(toInt(n, i))
            if (div == 0):
                break;
            divisors.append(str(div))
        if (len(divisors) == 9):
            print(n + " " +  " ".join(divisors))
            count += 1
            if (count == 50):
                break
        n = toInt(n, 2) + 2
        #print(n)
        coin = n



#print(str(get_divisor(53)))
#toInt(5, 10)
print("Case #1:")
process(16)

   
