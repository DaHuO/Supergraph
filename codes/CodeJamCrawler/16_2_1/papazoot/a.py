from Solve import *
import string
import itertools

nums = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
numsDictList = [{'R': 1, 'Z': 1, 'E': 1, 'O': 1}, {'E': 1, 'O': 1, 'N': 1}, {'O': 1, 'T': 1, 'W': 1}, {'H': 1, 'R': 1, 'E': 2, 'T': 1}, {'R': 1, 'U': 1, 'O': 1, 'F': 1}, {'I': 1, 'V': 1, 'E': 1, 'F': 1}, {'I': 1, 'X': 1, 'S': 1}, {'S': 1, 'N': 1, 'E': 2, 'V': 1}, {'I': 1, 'H': 1, 'E': 1, 'T': 1, 'G': 1}, {'I': 1, 'E': 1, 'N': 2}, {'R': 1, 'Z': 1, 'E': 1, 'O': 1}, {'E': 1, 'O': 1, 'N': 1}, {'O': 1, 'T': 1, 'W': 1}, {'H': 1, 'R': 1, 'E': 2, 'T': 1}, {'R': 1, 'U': 1, 'O': 1, 'F': 1}, {'I': 1, 'V': 1, 'E': 1, 'F': 1}, {'I': 1, 'X': 1, 'S': 1}, {'S': 1, 'N': 1, 'E': 2, 'V': 1}, {'I': 1, 'H': 1, 'E': 1, 'T': 1, 'G': 1}, {'I': 1, 'E': 1, 'N': 2}, {'R': 1, 'Z': 1, 'E': 1, 'O': 1}, {'E': 1, 'O': 1, 'N': 1}, {'O': 1, 'T': 1, 'W': 1}, {'H': 1, 'R': 1, 'E': 2, 'T': 1}, {'R': 1, 'U': 1, 'O': 1, 'F': 1}, {'I': 1, 'V': 1, 'E': 1, 'F': 1}, {'I': 1, 'X': 1, 'S': 1}, {'S': 1, 'N': 1, 'E': 2, 'V': 1}, {'I': 1, 'H': 1, 'E': 1, 'T': 1, 'G': 1}, {'I': 1, 'E': 1, 'N': 2}, {'R': 1, 'Z': 1, 'E': 1, 'O': 1}, {'E': 1, 'O': 1, 'N': 1}, {'O': 1, 'T': 1, 'W': 1}, {'H': 1, 'R': 1, 'E': 2, 'T': 1}, {'R': 1, 'U': 1, 'O': 1, 'F': 1}, {'I': 1, 'V': 1, 'E': 1, 'F': 1}, {'I': 1, 'X': 1, 'S': 1}, {'S': 1, 'N': 1, 'E': 2, 'V': 1}, {'I': 1, 'H': 1, 'E': 1, 'T': 1, 'G': 1}, {'I': 1, 'E': 1, 'N': 2}]

def phoneNumber(args):
    numS = args[0]
    charCounts = {}
    totalChars = 0
    
    for c in string.ascii_uppercase:
        charCounts[c] = 0
        
    for c in numS:
        charCounts[c] += 1
        totalChars += 1

    numbers = None
    startOffset = 0
    while numbers == None and startOffset < 10:
        numbers = findNumber(totalChars, startOffset, charCounts.copy())
        startOffset += 1
    if numbers == None:
        print "fuck"
    numbers.sort()
    phoneNumber = ""
    for n in numbers:
        phoneNumber += str(n)   
    return phoneNumber

def findNumber(totalChars, startOffset, charCounts):
    i = 0
    numbers = []
    maxN = len(nums)    
    while i < maxN and totalChars > 0:
        index = (i + startOffset) % maxN
        nDict = numsDictList[index]
        word = nums[index]
        hasAll = all([charCounts[c] >= nDict[c] for c in nDict.keys()])
        if hasAll:
            numbers.append(index)
            for c in word:
                charCounts[c] -= 1
                totalChars -= 1
        else:
            i+=1
    if totalChars == 0:
        return numbers
    else:
        return None
            
if __name__ == "__main__":
    solveF("A-large.in", phoneNumber, 1)
