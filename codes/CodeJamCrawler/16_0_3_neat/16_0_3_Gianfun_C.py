import pickle
try:
    pick = open("primes.pickle", "rb")
    primes = pickle.load(pick)
    pick.close()
except FileNotFoundError:
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

def isPrimeNumber(N):
#for i in range(2, 2**16, 2):
#for i in range(3, 2**24, 2):
    global primes
    minDiv = 0
#    print(N, "in isPrime")
    if N < primes[-1]: #is calculated
        
#        print("is smaller than largest in array")
        if N in primes:
            isNumPrime = True
        else:
            for prime in primes:
                if N%prime == 0:
                    minDiv = prime
                    break
            isNumPrime = False
    else: #calculate
        #Check if divisible by number in primes list
        isNumPrime = True
        for prime in primes:
            if N%prime == 0:
                minDiv = prime
                isNumPrime = False
                break

        if isNumPrime: #We did not find a divisor in primes list. Search
            if primes[-1] > int(N**0.5)+1:
                #List had all possible primes between 1 and sqrt(N)
                #Therefore, number is not prime
                pass
            else:
                #Lets search
                isNumPrime = True
                minDiv = -1;
                goingfrom = primes[-1]
                upto = 300000 #int(N**0.5)+1 #We dont need to find this prime. Go to next num
 #               print("loop from %d to %d"%(goingfrom, upto))
                for i in range(goingfrom, upto, 2):
                    if N%i == 0:
                        minDiv = i
                        isNumPrime = False
                        break
                    if i % (upto/100) == 0:
                        print( i / upto )
                    


#    print([isNumPrime, minDiv])
    return [isNumPrime, minDiv]

filename = "C-large"
f = open(filename + ".in", "r")
output = open(filename + ".out", "w")

T = int(f.readline().strip())

for idx in range(T):
    case = idx + 1

    N, J = [int(v) for v in f.readline().strip().split(" ")]
    print("N: ", N, "J: ", J)
    
    jamcoins = []
    for i in range(2**(N-2)):
        proponent = '1'+ bin(i)[2:].zfill(N-2) + '1'
        minDiv = 0
#        print(proponent)
        #check bases
        jam = [proponent]
        isJam = True
        for b in range(2, 10+1):
#            print("base: ", b)
            proponentInBaseN = int(proponent, b)
            if proponentInBaseN % 2 == 0: #is even
                jam.append(2)
                continue #is not prime, check next base
            else: #is odd, might be prime
                isPrime, minDiv = isPrimeNumber(proponentInBaseN)
                if minDiv == -1: #Gave up.
                    print("Giving up on proponent %s in base %d (value: %d)"%(proponent, b, proponentInBaseN))
                    break
#                print("ret from isPrime")
                if isPrime:
                    isJam = False
                    break #is prime, so it is not a jamcoin
                else:
                    jam.append(minDiv)
                    continue #is not prime in base b, check next
        if minDiv == -1:
            continue
        if isJam:
            print(len(jamcoins),"/", J)
            jamcoins.append(jam)
            if len(jamcoins) == J:
                break

#    print("jamcoins: ", jamcoins)

    output.write("Case #%d:\n"%case)
    for jam in jamcoins:
        for v in jam:
            print(str(v), end=" ")
            output.write(str(v) + " ")
        output.write("\n")
        print()
        

f.close()
output.close()

#Generate primes
if False:
    print("hi")
    try:
        pick = open("primes.pickle", "rb")
        primes = pickle.load(pick)
        pick.close()
    except FileNotFoundError:
        primes = [2, 3]

    for i in range(primes[-1], 10**16, 2):
        isNumPrime = True
        for prime in primes:
            if i%prime == 0:
                isNumPrime = False
                break
        if isNumPrime:
            primes.append(i)
            if len(primes) % 5000 == 0:
                print("writing to pickle")
                pick = open("primes.pickle", "wb") 
                pickle.dump(primes, pick)
                pick.close()
                print(i, "/", 10**16)
            
