import sys

def addOne(arr):
    carry = 1
    for i in range(len(arr))[::-1]:
        if arr[i] + carry == 2:
            arr[i] = 0
            carry = 1
        else:
            arr[i] += carry
            carry = 0
    return arr

def nonTrivialDivisors(num):
    for divisor in range(2, num):
        if num % divisor == 0:
            return divisor

def isPrime(num):
    if num in (2, 3):
        return True
    if num  % 2 == 0 or num <= 1:
        return False
    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
    return True

def numConverter(num, base):          # num given as a string
    num = str(num)
    decsum = 0
    for n in range(0, len(num)):
        decsum += int(num[n])*(base**(len(num)-1-n))
    return decsum

def coinJam(N, J):
    results = []
    start = [0]*N
    start[0], start[-1] = 1, 1
    num = start
    while sum(num) != N:
        num = [1] + addOne(num[1:-1]) + [1]
        strNum = ''.join(map(str, num))
        # print num
        isPrimes = []
        convertedNums = []
        for base in range(2, 11):
            convertedNum = numConverter(strNum, base)
            convertedNums.append(convertedNum)

            isPrimes.append(isPrime(convertedNum))
            if any(isPrimes):
                break
        if not any(isPrimes) and len(results) < J:
            divisors = map(nonTrivialDivisors, convertedNums)
            results.append(strNum + ' ' + ' '.join(map(str, divisors)))
    for res in results:
        print res

f = open(sys.argv[1], 'r')
num = f.readline().strip()
N, J = map(int, f.readline().strip().split())
print 'Case #1:'
coinJam(N, J)
