import itertools

def prime(N):
    dividor = 0
    if N <= 1:
        dividor = 1
        return [False, dividor]
    elif N <= 3:
        return [True, dividor]
    elif N%2 == 0:
        dividor = 2
        return [False, dividor]
    elif N%3 == 0:
        dividor = 3
        return [False, dividor]
    
    i = 5
    # while i*i <= N:
    while i*i <= N and i <= 10000000:
        if N%i == 0:
            dividor = i
            return [False, dividor]
        elif N%(i + 2) == 0:
            dividor = i + 2
            return [False, dividor]
            
        i = i + 6
        
    return [True, dividor]
    
def convertBase(N, baseNumber):
    n = 0
    pow = 0
    for i in N[::-1]:
        n = n + int(i) * baseNumber ** pow
        pow = pow + 1
        
    return n
    
def findNonTrivialDividor(i):
    for b in range(2,11):
        convertedI = convertBase(i,b)

    
def main():
    T = int(raw_input())
    print "Case #{}:".format(T)
    [N, J] = [int(i) for i in raw_input().split(" ")]
    
    amountFound = 0
    
    for i in itertools.product(*[[0,1]]*(N-2)):
        i = (1,) + i + (1,)
        
        # check if not a prime in all bases
        primeBoolean = False
        dividors = [0] * 9
        for b in range(2,11):
            convertedI = convertBase(i,b)
            [primeBoolean, dividors[b-2]] = prime(convertedI)
            
            if primeBoolean:
                break
                
        # if not a prime
        if not primeBoolean:
            amountFound = amountFound + 1
            print "{} {}".format("".join([str(j) for j in i]), " ".join([str(j) for j in dividors]))
        
        if amountFound == J:
            break
            
if __name__ == "__main__":
    main()                    
        