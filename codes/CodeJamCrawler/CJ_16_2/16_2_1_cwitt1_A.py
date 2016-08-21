
numbers = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

T = int(input())

def canUseNumber(num, chars):
    chars_copy = chars.copy()
    for c in numbers[num]:
        if c in chars_copy and chars_copy[c] > 0:
            chars_copy[c] -= 1
        else:
            return False

    for k in chars_copy:
        chars[k] = chars_copy[k]

    return True

def lettersLeft(chars):
    for c in chars:
        if chars[c] > 0:
            return True
            break

    return False

def restoreNum(chars, num):
    numtext = numbers[num]

    for c in numtext:
        chars[c] += 1

for i in range(1, T+1):
    S = input()

    chars = {}

    for c in S:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1

    number = ""

    num = 0
    while num < 10:
        while canUseNumber(num, chars):
            number += str(num)

        if num == 9 and lettersLeft(chars):
            lastNum = int(number[-1])
            restoreNum(chars, lastNum)
            num = lastNum + 1
            number = number[:-1]
        else:
            num += 1
            continue


    #print(chars)
    print("Case #{}: {}".format(i, number))
