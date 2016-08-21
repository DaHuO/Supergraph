# I wrote the program to run with PyPy, so it may be somewhat slower with CPython.

def decode(inputstring):

    numbers = (("Z","ZERO"), ("W", "TWO"), ("X", "SIX"), ("G", "EIGHT"), ("H", "THREE"), ("R", "FOUR"), ("F", "FIVE"), ("O", "ONE"), ("S", "SEVEN"), ("I", "NINE"))

    letterQty = {}

    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        letterQty[letter] = 0

    hashTable = {"Z": 0, "W": 2, "X": 6, "G": 8, "H": 3, "R": 4, "F": 5, "O": 1, "S": 7, "I": 9}


    for letter in inputstring:
        letterQty[letter] = letterQty[letter]+1

    result = [0,]*10

    i = 0
    while i < len(numbers):
        if letterQty[numbers[i][0]] > 0:
            result[hashTable[numbers[i][0]]] = letterQty[numbers[i][0]]
            safe = letterQty[numbers[i][0]]
            for letter in numbers[i][1]:
                letterQty[letter] = letterQty[letter] - safe
        i = i + 1

    resultString = ""

    i = 0
    while i < len(numbers):
        resultString = resultString + result[i]*str(i)
        i = i + 1

    return resultString

with open("puhelinnumerot.txt", "r") as f:
    i = 1
    f.readline()
    for line in f:
        print("Case #"+str(i)+": "+decode(line.strip("\n")))
        i = i + 1
