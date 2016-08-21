from math import sqrt; from itertools import count, islice
from multiprocessing import Pool

def isPrime(n):
    return all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def firstNontrivial(n):
    return next((i for i in islice(count(2), int(sqrt(n)-1)) if n%i==0),False)

def checkJamCode(possibility):
    #jamcoin = '1' + bin(possibility)[2:] + '1'
    jamcoin = '1' + "{0:04b}".format(possibility) + '1'
    all_not_prime = [not isPrime(int(jamcoin,i)) for i in range(2,11)]
    is_jamcoin = all(item == True for item in all_not_prime)
    if is_jamcoin:
        return jamcoin
    else:
        return False

def checkJamCodePlus(possibility):
    jamcoin = '1' + "{0:014b}".format(possibility) + '1'

    non_trivials = [firstNontrivial(int(jamcoin,i)) for i in range(2,11)]
    is_jamcoin = not any(item==False for item in non_trivials)
    if is_jamcoin:
        return jamcoin+' '+' '.join([str(nt) for nt in non_trivials])
    else:
        return False

def findAllJamCoins(length=16,output_file='jamcoin.out'):
    number_of_possibilities = int('1'*(length-2),2) + 1 # all zeros
    print number_of_possibilities

    output_data = []
    pool = Pool(processes=50)
    for i, status in enumerate(pool.imap_unordered(checkJamCodePlus, range(number_of_possibilities))):
        if status:
            print status
            output_data.append(status)

    open(output_file,'w').write('\n'.join(output_data))