from code_jam import *
from copy import deepcopy

numbers = ['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'ZERO']
numbers_map = {
    "ONE": 1,
    "TWO": 2,
    "THREE": 3,
    "FOUR": 4,
    "FIVE": 5,
    "SIX": 6,
    "SEVEN": 7,
    "EIGHT": 8,
    "NINE": 9,
    "ZERO": 0
}

def done(input):
    for item in input:
        if input[item] > 0:
            return False
    return True

def strip(number, input):
    for char in number:
        if char not in input or input[char] == 0:
            return False
        input[char] -= 1
    return input

def subsolve(input, results):
    # print("starting to solve " + str(input))
    if done(input):
        # print("done, returning " + str(results))
        return results
    for number in numbers:
        stripped = strip(number, deepcopy(input))
        if not stripped:
            continue
        # print("stripped: ")
        # print(stripped)
        rescopy = deepcopy(results)
        rescopy.append(numbers_map[number])
        res = subsolve(stripped, rescopy)
        if res:
            return res
    # print(input)
    return False

@autosolve
@collects
def solve(tokens):
    letters = {}
    input = tokens.next_token(str)
    for char in input:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    
    # print(letters)

    reslist = subsolve(letters, [])
    reslist.sort()
    return ''.join(map(str, reslist))
