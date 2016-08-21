__author__ = 'Kirby'

import random

def charCount(string):
    dict = {}
    for char in string:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

def pullWordsHelper(toNumDict, toWordDict, lettersDict):
    nums = []
    for key in toNumDict:
        if key in lettersDict:
            count = lettersDict[key]
            for i in range(count):
                nums.append(toNumDict[key])
            letters = toWordDict[key]
            for letter in letters:
                lettersDict[letter] -= count
                if lettersDict[letter] == 0:
                    del lettersDict[letter]

    return (nums, lettersDict)



'''
Unique letters:
    G -> 8
    X -> 6
    W -> 2
    Z -> 0
    U -> 4

Twos:
    S -> 6, 7     but an S w/o a matching X -> 7
    V -> 5, 7     V w/o a matching S -> 5
    H -> 3, 8     H w/o matching G -> 3
    F -> 4, 5     F w/o matching U -> 5

What's left is 9 and 1 so:
    O -> 1
    I -> 9
'''
def pullWords(charFreq):
    uniquesToNum = {'G': 8, 'X': 6, 'W': 2, 'Z': 0, 'U': 4}
    uniquesToWord = {'G': 'EIGHT', 'X': 'SIX', 'W': 'TWO', 'Z': 'ZERO', 'U': 'FOUR'}
    nums = []

    # pull uniques
    (tempNums, charFreq) = pullWordsHelper(uniquesToNum, uniquesToWord, charFreq)
    nums = nums + tempNums

    # pull post-unique indicators
    postUniquesToNum = {'S': 7, 'H': 3, 'F': 5}
    postUniquesToWord = {'S': 'SEVEN', 'H': 'THREE', 'F': 'FIVE'}
    (tempNums, charFreq) = pullWordsHelper(postUniquesToNum, postUniquesToWord, charFreq)
    nums = nums + tempNums

    finalsToNum = {'O': 1, 'I': 9}
    finalsToWord = {'O': 'ONE', 'I': 'NINE'}
    (tempNums, charFreq) = pullWordsHelper(finalsToNum, finalsToWord, charFreq)
    nums = nums + tempNums

    return nums


def largeTestCase():
    numbers = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    testString = ""
    totalLen = 0

    while totalLen < 2000:
        num = random.choice(numbers)
        testString += num
        totalLen += len(num)

    return pullWords(charCount(testString))

def testLarge():
    for i in range(100):
        print(sorted(largeTestCase()))


if __name__=="__main__":
    with open("test.txt", "r") as f:
        T = int(f.readline())
        with open("results.txt", "w") as fo:
            for i in range(T):
                string = "Case #{0}: {1}".format(i+1, "".join(str(num) for num in sorted(pullWords(charCount(f.readline())))))
                fo.write(string)
                fo.write("\n")



