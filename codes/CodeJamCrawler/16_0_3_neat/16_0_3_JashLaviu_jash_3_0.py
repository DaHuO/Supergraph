"""
problema 3
"""
import math 


def getPrimeList(maxNumber):
    primes = [2]
    number = 3
    while number < maxNumber:
        for div in primes:
            if div >= int(math.sqrt(number)) + 1:
                isPrime = True
                break
            if number % div == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(number)
        number += 2
    return primes


def getDivisor(n, primes):
    divisor = 0
    if n > 3:
        for i in primes:
            if i > math.sqrt(n):
                break
            if n % i == 0:
                divisor = i
                break
    return int(divisor)


def nextJamcoin(jamcoin):
    jamcoin_str = bin(int(jamcoin ,2) + int('1',2))
    return jamcoin_str[2:]


def goodOutput(jamcoins, d):

    for i in range(0, len(jamcoins)):
        print jamcoins[i],
        for j in range(0, 9):
            print d[i][j],

        print ""

 #       print "{} {} {} {} {} {} {} {} {} {}".format(jamcoins[i], d[i][0], d[1][i], d[i][2], d[i][3], d[i][4], d[i][5], d[i][6], d[i][7], d[i][8])



def dameRes(largo_jamcoin, MAXIMOS):

    #primes = getPrimeList(int("1"*largo_jamcoin)+1)
    primes = getPrimeList(int(math.sqrt(int("1"*13))))

    current_jamcoin = "1" + "0"*(largo_jamcoin-1)
    max_jamcoin = '1'*largo_jamcoin

    all_jamcoins = []
    all_divisors = []

    while current_jamcoin != max_jamcoin:
        current_jamcoin = nextJamcoin(current_jamcoin)
        current_divisors = []
        isFake = False

        if current_jamcoin[0] == '0':
            isFake = True
        if current_jamcoin[largo_jamcoin-1] == '0':
            isFake = True

        if not isFake:
            for b in range(2, 11):
                jamcoin_b = int(current_jamcoin, b)
                a_divisor = getDivisor(jamcoin_b, primes)

                if a_divisor == 0:
                    isFake = True
                    break
                else:
                    current_divisors.append(a_divisor)

        if not isFake:
            all_jamcoins.append(current_jamcoin)
            all_divisors.append(current_divisors)
            #print all_jamcoins


        if len(all_jamcoins) == int(MAXIMOS):
            break


    # Devolver una string con el output esperado, BIEN HECHO. forma:
    # JAMCOIN Db2 Db3 Db4 ... Db10
    goodOutput(all_jamcoins, all_divisors)



t = int(raw_input())
for ti in range(1, t+1):
    casoActual = [s for s in raw_input().split(" ")]
    casoActual[0] = int(casoActual[0])
    print "Case #{}:".format(ti)
    dameRes(casoActual[0], casoActual[1])