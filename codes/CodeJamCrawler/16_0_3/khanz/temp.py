from math import sqrt
def toDecimal(n, b):
    result = 0
    i = 0
    while n!=0:
        result += (n%10)*(b**i)
        n //= 10
        i += 1
    return result

def getDevisor(n):
    for i in range(2, int(sqrt(n))):
        if n%i == 0:
            return i

def binaryAdd2(n):
    n = str(n)
    for i in range(len(n)-2, -1, -1):
        if n[i] == '0':
            break
    return int(n[:i]+'1'+'0'*(len(n) - i-2)+'1')

def main():
    n = int(input())
    N = []
    J = []
    for i in range(n):
        line = input().split(' ')
        N.append(int(line[0]))
        J.append(int(line[1]))
    for i in range(n):
        print("Case #1:")
        currNum = 10**(N[i]-1)+1
        for j in range( J[i] ):
            while(True):
                devisors = []
                for k in range(2, 11):
                    d = getDevisor(toDecimal(currNum, k))
                    if d:
                        devisors.append(d)
                    else:
                        break
                if len(devisors) == 9:
                    result = str(currNum)
                    for k in devisors:
                        result += ' '+str(k)
                    print(result)
                    currNum = binaryAdd2(currNum)
                    break
                else:
                    currNum = binaryAdd2(currNum)

if __name__ == "__main__":
    main()
