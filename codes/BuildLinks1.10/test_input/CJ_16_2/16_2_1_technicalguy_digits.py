#!/usr/bin/env python
import fileinput

def digits(string):
    string = string[0:-1]
    letters = {}
    numbers = [0 for i in range(10)]
    def subtract(keyletter, name):
        result = letters[keyletter]
        for char in name:
            letters[char] -= result
        return result
    for c in range(ord('A'), ord('Z') + 1):
        letters[str(chr(c))] = 0
    for char in string:
        letters[char] += 1

    numbers[0] = subtract("Z", "ZERO")
    numbers[2] = subtract("W", "TWO")
    numbers[4] = subtract("U", "FOUR")
    numbers[6] = subtract("X", "SIX")
    numbers[8] = subtract("G", "EIGHT")

    # second pass
    numbers[1] = subtract("O", "ONE")
    numbers[3] = subtract("H", "THREE")
    numbers[5] = subtract("F", "FIVE")
    numbers[7] = subtract("V", "SEVEN")

    # third pass
    numbers[9] = subtract("I", "NINE")

    error = False
    for key, value in letters.iteritems():
        if value != 0:
            error = True
            break
    if error:
        print string
        print letters
        raise Exception("did not subtract cleanly")

    result = ""
    for index, value in enumerate(numbers):
        result += str(index) * value

    return result

i = 0
for line in fileinput.input():
    if i == 0:
        i += 1
        continue
    print("Case #" + str(i) + ": " + str(digits(line)))
    i += 1
