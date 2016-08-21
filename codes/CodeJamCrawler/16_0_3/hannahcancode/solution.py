O = open('output.txt', 'w')
import random
N = 16
J = 50
allcoins = []
cases = 1

binarystartlist = []
for x in range(16):
    binarystartlist.append('1')
binarystart = ''.join(binarystartlist)
startingnumber = int(binarystart, base=2)

def convert(coin, base):
    digs = '0123456789'
    digits = []
    while coin > 0:
        digits.append(digs[coin % base])
        coin /= base
    digits.reverse()
    return ''.join(digits)
    
def checkprime(n):
    n = int(n)
    divisor = 0
    if n/2 == 0: 
        return False, 2
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False, x
            break
        else: divisor = x
    return True, divisor
    
def cointest(coin):
    isjamcoin = True
    newcoinlist = []
    newcoin10 = str(coin)
    for x in range(2, 11):
        coininbase = int(newcoin10, x)
        isprime, divisor = checkprime(coininbase)
        if isprime == False:
            newcoinlist.append(str(divisor))
        else:
            isjamcoin = False
            break
    return isjamcoin, newcoinlist

count = 0
while len(allcoins) < J:
    x = convert(startingnumber-count, 2)
    isjamcoin, newcoinlist = cointest(x)
    if isjamcoin == True:
        if x in allcoins:
            break
        else:
            newlist = []
            newlist.append(str(x))
            for i in newcoinlist:
                newlist.append(i)
            allcoins.append(newlist)
    count += 2

O.write("Case #"+str(cases)+":\n")
for i in allcoins:
    k = ' '.join(i)
    O.write(k+"\n")

O.close()