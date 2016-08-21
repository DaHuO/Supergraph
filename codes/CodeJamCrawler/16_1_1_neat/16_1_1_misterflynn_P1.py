from array import *

def GetLowestLastWord(letters):
    numLetters = len(letters)
    lowestLastWord = [letters[0]]

    for i in range(1, numLetters):
        letter = letters[i]
        if letter >= lowestLastWord[0]:
            lowestLastWord.insert(0, letter)
        else:
            lowestLastWord.append(letter)

    return lowestLastWord

numTests = int(raw_input())
for i in range(1, numTests + 1):
    letters = list(raw_input())
    lowestLastWord = GetLowestLastWord(letters)

    str = ""
    for j in range(0, len(lowestLastWord)):
            str += (lowestLastWord[j])
    print("Case #{}: {}".format(i, str))
