import itertools

input_lines = []
output_lines = []

with open('input.txt', 'r') as input:
    data = input.read()

input_lines = data.split('\n')

NUMBERS = ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE")

_M = {
    "ZERO" : 0,
    "ONE" : 1,
    "TWO" : 2,
    "THREE" : 3,
    "FOUR" : 4,
    "FIVE": 5,
    "SIX" : 6,
    "SEVEN" : 7,
    "EIGHT" : 8,
    "NINE" : 9
}

__M = {
    'Z' : [0],
    'W' : [2],
    'H' : [3, 8],
    'U' : [4],
    'X' : [6],
    'S' : [7], # remove 'X' Counts
    'V' : [5], # remove 7 count
    'N' : [1, 9],  # remove 7 count
    'O' : [0, 1, 2, 4],
    'R' : [0, 3, 4],
    'G' : [8],
    'N' : [1, 7, 9],
    'I' : [6, 8, 9],
    'E' : [0,1,3,5,7,8,9]

}

_M = {
    "ONE" : 'ONE',
    "FIVE": 5,
    "SIX" : 6,
    "SEVEN" : 7,
    "NINE" : 9
}


def decode_pattern(pattern):
    output = []
    pattern = ''.join(pattern)
    start_index = 0
    while start_index < len(pattern):
        pKey = pattern[start_index:start_index+3]
        if pKey in _M:
            output.append(str(_M[pKey]))
            start_index += 3
            continue

        pKey = pattern[start_index:start_index+4]

        if pKey in _M:
            output.append(str(_M[pKey]))
            start_index += 4
            continue

        pKey = pattern[start_index:start_index+5]

        if pKey in _M:
            output.append(str(_M[pKey]))
            start_index += 5
            continue

        return False

    if start_index == len(pattern):
        return ''.join(output)

    return False

def rdecode(arr):
    output = []
    for i in arr:
        output.append(NUMBERS[i])

    output = ''.join(output)

    return ''.join(sorted(output))

CACHE = {}

def init(start, target):

    if start == 4:
        CACHE[rdecode(target)] = target
        return

    for index in xrange(start, 4):
        n_target = target[:]
        n_target.append(index)
        init(index+1, n_target)

        n_target = target[:]
        init(index+1, target)


case = 0
init(0, [])
n_c = {}

for a_input in input_lines[1:]:
    case += 1
    # print decode_pattern(['O', 'N', 'E', 'F', 'O', 'U', 'R', 'T', 'H', 'R', 'E', 'E'])

    for c in xrange(65, 91):
        n_c[chr(c)] = 0

    for c in a_input:
        n_c[c] += 1

    n0 = n_c['Z']
    n1 = n_c['O']
    n2 = n_c['W']
    n3 = n_c['H']
    n4 = n_c['U']
    n5 = n_c['V']
    n6 = n_c['X']
    n7 = n_c['S']
    n8 = n_c['G']
    n9 = n_c['I']

    if n7  > 0:
        n7 -= n6

    if n5 > 0:
        n5 -= n7

    if n1 > 0:
        n1 -= (n0 + n2 + n4)

    if n3> 0:
        n3 -= n8

    if n9> 0:
        n9 -= (n6 + n8 + n5)

    freq = [n0, n1, n2, n3, n4, n5, n6, n7, n8, n9]

    output = []


    for index in xrange(10):
        if freq[index]:
            output += [index]*freq[index]

    value = ''.join(map(str, output))
    output_lines.append('Case #%s: %s' % (case, value))

data = '\n'.join(output_lines)
with open('output.txt', 'w') as output:
    output.write(data)

