
def convertVal(val, base):
    result = 0
    i = 0
    while (val > 0):
        result += (val % 10) * pow(base, i)
        val /= 10
        i = i+1
    return result
    
def incrementVal(val):
    result = 0
    val = convertVal(val, 2)
    val += 2
    
    i = 0
    
    while (val > 0):
        result += pow(10, i) * (val & 0x01)
        val = val >> 1
        i = i+1
    
    return result
    
print "Case #1: "

val = 10000000000000000000000000000001
prime = False

sieve = [False] * 10000000
primes = []

sieve[0] = True
sieve[1] = True

for i in range(2, 10000000):
    if sieve[i] == False:
        for j in range (i + i, 10000000, i):
            sieve[j] = True
            
for i in range(0, 10000000):
    if sieve[i] == False:
        primes.append(i)
           
J = 0
vals = [0] * 11

while (val < 11111111111111111111111111111111 and J < 500):
    for i in range(0, len(primes)):
        if (not (val % primes[i]) and val != primes[i]):
            vals[10] = primes[i];
            break
        
        if (i + 1 == len(primes)):
            prime = True
        
    for base in range(2, 11):
        if prime == True:
            break
        
        converted = convertVal(val, base)
        
        for i in range(0, len(primes)):
            if (not (converted % primes[i]) and converted != primes[i]):
                vals[base] = primes[i];
                break
        
            if (i + 1 == len(primes)):
                prime = True        
            
    if (prime == False):
        string = str(val) + " "
        
        for i in range(2, 11):
            string += str(vals[i]) + " " 
        
        print string
        J = J + 1
    
    val = incrementVal(val)
    prime = False
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    