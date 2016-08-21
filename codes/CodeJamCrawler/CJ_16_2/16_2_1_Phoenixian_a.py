def answer (response, casenumber):
    print("Case #" + str(casenumber) + ": " + str(response))

def pullOut (letter, digit, digitWord, scramble):
    newScramble = scramble
    currentNumbers = []
    while (newScramble.find(letter) != -1):
        for char in digitWord:
            newScramble = newScramble.replace(char, "", 1)
        currentNumbers.append(digit)
    return newScramble, currentNumbers

cases = eval(input())
uniquesList = ['Z', 'W', 'U', 'X', 'G', 'O', 'R', 'F', 'V', 'I']
digitsList = [0,2,4,6,8,1,3,5,7,9]
wordsList = ['ZERO', 'TWO', 'FOUR', 'SIX', 'EIGHT', 'ONE', 'THREE', 'FIVE', 'SEVEN', 'NINE']
for case in range(1, cases + 1):
    scramble = str(input())
    number = []
    addednumbers = []
    for unique, digit, word in zip(uniquesList, digitsList, wordsList):
        scramble, addednumbers = pullOut(unique, digit, word, scramble)
        number.extend(addednumbers)
    number.sort()
    response = ''
    for bit in number:
        response += str(bit)
    answer(response, case)
