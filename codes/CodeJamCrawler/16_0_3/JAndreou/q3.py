import math
T = int(raw_input())
print 'Case #' + str(T) + ':'

LINE = raw_input().split(' ')
N = int(LINE[0])
J = int(LINE[1])

possibleNumbers = pow(2, (N - 2))
# my python is horrible, but felt like trying it
i = possibleNumbers - 1;
while i >= 0 :
    num = bin(i)[2:]
    #pad with zeros
    for pad in range(0, N-2-len(num)):
        num = '0' + num
    num = '1' + num + '1'
    output = num
    # all bases
    isJam = False
    # Low probability if we havnt found yet lets move on to save time, this is around 65k divisors
    stopHere = int(math.floor(math.sqrt(int(num, 2))))
    for base in range(2, 11):
        baseNum = int(num, base)
        isJam = False
        n = 2
        while n < stopHere:
            if baseNum % n == 0:
                output = output + ' ' + str(n)
                isJam = True
                break
            n = n + 1
        if not isJam:
            break
    if isJam:
        print output
        J = J - 1
    if J == 0:
        break;
    i = i - 1
