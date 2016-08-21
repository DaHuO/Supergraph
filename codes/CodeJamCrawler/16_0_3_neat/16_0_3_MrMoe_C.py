

divisors = {}

def computeDivisor(n):
    if n == 2 or n == 3 or n < 2:
        return None
    if n%2 == 0:
        return 2
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            return i
    return None

def getDivisor(n):
    factor = divisors.get(n, False)
    if factor == False:
        factor = computeDivisor(n)
        divisors[factor] = n
    return factor

def jamcoins(N):
    for i in range(2**(N-2)):
        yield "1%s1" % (bin(i)[2:]).zfill(N-2)


T = int(input())

for t in range(T):
    N, J = tuple(map(int, input().split()))
    
    print("Case #%d:" % (t+1))
    
    j = 0
    for jamcoin in jamcoins(N):
        
        factors = []
        for base in range(2, 11):
            div = getDivisor(int(jamcoin, base))
            if div is None:
                break
            factors.append(div)
        else:
            print(jamcoin, " ".join(map(str, factors)))
            j += 1
        
        if j == J:
            break




