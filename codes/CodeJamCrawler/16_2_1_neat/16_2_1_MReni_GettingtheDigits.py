import collections
import copy

DIGITS = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

DEBUG = False

def hasdigit(letterset, digit):
    for char in digit:
        if letterset[char] <= 0:
            return False
    return True

def takeoutdigit(letterset, digit):
    for char in digit:
        letterset[char] -= 1

def checkfinished(letterset):
    for i in range(0, 25):
        if letterset[chr(ord('A') + i)] > 0:
            return False
    return True

def work2(old_letterset, start):
    # Check if finished
    if checkfinished(old_letterset):
        return ""
    for i in range(start, len(DIGITS)):
        letterset = copy.deepcopy(old_letterset)
        digit = DIGITS[i]
        if hasdigit(letterset, digit):
            takeoutdigit(letterset, digit)
            rest = work2(letterset, i)
            if rest != False:
                return str(i) + rest
    return False

def work(line):
    #parse
    letterset = collections.defaultdict(int)
    for char in line:
        letterset[char] += 1

    return work2(letterset, 0)

count = 1
results = []
filename = 'A-small-attempt0'
with open(filename + '.in', 'rb') as data:
    data.readline()
    for line in data:
        result = "Case #" + str(count) + ": " + str(work(line.replace('\n', ''))) 
        if DEBUG:
            print result
        results.append(result)
        count = count + 1

if not DEBUG:
    with open(filename + '.out', 'wb') as output_file:
        for result in results:
            output_file.write(result + '\n')
