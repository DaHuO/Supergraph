infile = open('input.in','r')
outfile = open('output.out','w')


def tobase(n,jamcoin):
    jamcoin.reverse()
    num = 0
    for i in range(len(jamcoin)):
        num += jamcoin[i] * n ** i
    jamcoin.reverse()
    return num

def getfirstdivisor(n,max):
    for i in range(2,max):
        if n%i==0:
            return i
    return n

def finddivisors(jamcoin,max):
    divisors = []
    for i in range(2, 11):
        n = tobase(i, jamcoin)
        d = getfirstdivisor(n,max)
        if n != d:
            divisors.append(d)
        else:
            return None
    return divisors

def next(jamcoin):
    jamcoin.reverse()
    for i in range(1,len(jamcoin)-1):
        if jamcoin[i]==0:
            jamcoin[i] = 1
            break
        else:
            jamcoin[i] = 0
    jamcoin.reverse()

N = 32
J = 500

jamcoin = []
for i in range(N):
    if i==0 or i==N-1:
        jamcoin.append(1)
    else:
        jamcoin.append(0)

count = 0
outfile.write('Case #1:\n')
while count < J:
    div = finddivisors(jamcoin,1000000)
    if div != None:
        print(jamcoin)
        print(div)
        count +=1
        for n in jamcoin:
            outfile.write(str(n))
        for d in div:
            outfile.write(' ')
            outfile.write(str(d))
        outfile.write('\n')
    next(jamcoin)


infile.close()
outfile.close()