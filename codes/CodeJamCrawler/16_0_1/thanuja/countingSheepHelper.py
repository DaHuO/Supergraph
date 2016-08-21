'''
Created on Apr 9, 2016

@author: thanuja
'''
# import numpy as np

def intersectLists(a, b):
    """
    Returns the intersection of lists a and b
    """
    return list(set(a) & set(b))

def countSheep(N):
    """
    Starting from n, up to which number N should we go to see all digits 0-9 at least once
    N is returned. If it's not plausible, 0 is returned
    """
    if(N==0):
        return 'INSOMNIA'
    else:
        unseenDigitsList = range(10)
        k = 1        
        while (unseenDigitsList):
            n = k * N
            # print n
            nDigitList = list(int(d) for d in str(n))
            digitsSeenList = intersectLists(unseenDigitsList, nDigitList)
            # digitsDict = updateDictWithDigitsSeen(digitsDict,digitsSeenList)
            newUnseenDigitsList = [d for d in unseenDigitsList if d not in digitsSeenList]
            unseenDigitsList = newUnseenDigitsList
            k = k+1
        
    return str(n)
    