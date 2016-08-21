import math

def tostr(arr):
    number = map(str, arr)
    number = "".join(number)
    return number

def to_base10(fromBase, digits):
    digits = list(map(int, digits))
    digits.reverse()
    base10 = 0
    pangkat = 0
    for i in digits:
        base10 += i * fromBase**pangkat
        pangkat += 1
        
    return base10

def is_notPrime(number):
    if number % 2 == 0:
        return 2
    nn = 1000
    for i in range(3, int(nn) + 1, 2):
        if number % i == 0:
            return i
    return False

T = int(input())
for tc in range(1,T+1):
    N, J = input().split(' ')
    N = int(N)
    J = int(J)
    print("Case #{0}:".format(tc))
    
    arrN = [0 for i in range(0, N)]
    arrN[0] = 1
    arrN[N-1] = 1
    
    arrN = tostr(arrN)
    
    base = [0 for i in range(2,11)]
    nontrivial = [0 for i in range(2,11)]
    bawah = to_base10(2, arrN)
    atas = (bawah - 1) * 2 -1
    
    for jj in range(J):
        #for a in range(bawah, atas+1): 1000000000000010 failed
        for a in range(bawah, atas+1, 2):
            arrN = bin(a)[2:]
            for i in range(len(base)):
                base[i]= to_base10(i+2, arrN)
                number = is_notPrime(base[i])
                if not number:
                    break
                else:
                    nontrivial[i] = number
            if not (nontrivial[i] == 0) and number:
                print(arrN, end=' ')
                for i in nontrivial[:-1]:
                    print(i, end=' ')
                print(nontrivial[-1])
                base = [0 for i in range(2,11)]
                nontrivial = [0 for i in range(2,11)]
                #bawah = a + 1 --> 1000000000000010 failed
                bawah = a + 2
                break