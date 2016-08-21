'''
Created on Apr 9, 2016

@author: thanuja
'''

import numpy as np
import math

def writeDictToFile(fout,jamCoinDict,i):
    str1 = 'Case #' + str(i+1) + ':\n'
    fout.write(str1)
    for key in jamCoinDict:
        factorList = jamCoinDict[key]
        factorString = ' '.join('%s' % i for i in factorList)
        str2 = key + ' ' +factorString + '\n'
        fout.write(str2)
        


def factors(n):    
    # factorSet = set(reduce(list.__add__, 
    #             ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    
    factorList = []
    # j = 0;
    for i in range (2, int(n**0.5) +1):
        if(n % i == 0):
            factorList = [i, n//i]
            break
    
    #factorList = list(factorSet)
    # remove 1 and n from the set
    # factorList.remove(1)
    # factorList.remove(n)
    return factorList
    
    
def printDictionary(cars):
    for x in cars:
        print (x)

def getJamCoinsBase2(N):
    """
    Calculates jam coins in base 2 for a given string length N
    First and last digits are 1
    """
    
    # variable middle part of a jam String
    maxMiddleArray = np.ones(N-2)  
    maxMiddleString = ''.join(['%s' % i for i in maxMiddleArray.astype(int)])
    maxNum = int(maxMiddleString,2)
    
    jamCoinsDict = {}
    
    for i in range(0,maxNum+1):
        formatStr = '#0' + str(N) + 'b'
        middleBinString = format(i, formatStr).split('b')[1]
        jamString = '1' + middleBinString + '1'
        decNumber = int(jamString,2)
        
        factorsList = factors(decNumber)
        if(factorsList):
            jamCoinsDict[jamString] = list(factorsList)[0]
            # print decNumber
            #print factorSet
    
    return jamCoinsDict
        
def getFactorForJamCoin(jamCoin,base):
    """
    For a give jam coin, in a given base, return a factor if it has, or return 0
    """
    decVal = int(jamCoin,base)
    factorsList = factors(decVal)
    # print factorsList
    if(not factorsList):
        return 0
    else:
        return factorsList[0]


def getJamCoins(N,J):
    
    """
    N - number of bits in the jamcoin. First bit and last bit are always 1
    J - number of jamcoins required
    """

    # first look for potential jam coins starting from base 2. also store one factor
    # then for these strings, check if they are still jamcoins for other bases 3,4, etc.
    # if they are not remove them from the dict

    jamCoinsDictInit = getJamCoinsBase2(N)
    jamCoinsDictFinal = {}
    #print jamCoinsDict
    j = 0 # index to keep track of currently valid jamcoins
    for key in jamCoinsDictInit:
        if(j<J):
            jFactors = []
            jFactors.append(jamCoinsDictInit[key]) 
            for base in range(3,11):
                # for the currently chosen jam coins (up to previously checked base, retain them as long as they are jam coins for this base
                # check up to J number of such feasible jam coins
                factorForBase = getFactorForJamCoin(key,base)
                # print factorForBase
                if(factorForBase==0):
                    break
                else:
                    jFactors.append(factorForBase)
            if(len(jFactors)==9):
                jamCoinsDictFinal[key] = jFactors
                j = j+1
    
    
    return jamCoinsDictFinal


        
    

    