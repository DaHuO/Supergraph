##
## Google Code Jam 2016
## Round 1B, Apr 30
##
## Problem Title: Getting the digits
## Author: James Hall
## Email: james.hall@infinityworks.com
##

numbers = {
    0: "ZERO",
    1: "ONE",
    2: "TWO",
    3: "THREE",
    4: "FOUR",
    5: "FIVE",
    6: "SIX",
    7: "SEVEN",
    8: "EIGHT",
    9: "NINE"
}

def remove_first_set(param):

    count = 0
    nums = []

    while True:
        if "Z" in param:
            param = remove_number(0, param)
            nums += [0]
            count += 1
        if "W" in param:
            param = remove_number(2, param)
            nums += [2]
            count += 1
        if "U" in param:
            param = remove_number(4, param)
            nums += [4]
            count += 1
        if "X" in param:
            param = remove_number(6, param)
            nums += [6]
            count += 1
        if "G" in param:
            param = remove_number(8, param)
            nums += [8]
            count += 1
        if count == 0:
            break
        count = 0

    return [param, nums]

def remove_second_set(param):

    count = 0
    nums = []

    while True:
        if "O" in param:
            param = remove_number(1, param)
            nums += [1]
            count += 1
        if "T" in param:
            param = remove_number(3, param)
            nums += [3]
            count += 1
        if "S" in param:
            param = remove_number(7, param)
            nums += [7]
            count += 1
        if "F" in param:
            param = remove_number(5, param)
            nums += [5]
            count += 1
        if count == 0:
            break
        count = 0

    return [param, nums]

def remove_third_set(param):
    
    count = 0
    nums = []

    while param != []:
        param = remove_number(9, param)
        nums += [9]
        count += 1

    return [param, nums]
    
def remove_number(x, word):

    letters = numbers[x]
    for c in letters:
        word.remove(c)

    return word

def calculate(param):

    result = []
    
    [param, nums] = remove_first_set(param)
    result += nums

    if param != []:
        [param, nums] = remove_second_set(param)
        result += nums
    if param != []:
        [param, nums] = remove_third_set(param)
        result += nums

    return "".join([str(i) for i in sorted(result)])
    
if __name__ == "__main__":
    t = int(input())
    for i in range(1, t + 1):
        params = [s for s in input()]
        result = calculate(params)
        print("Case #{}: {}".format(i, result))
