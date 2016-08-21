import re, sys
array = []
with open('input.txt') as f:
    numCases = int(next(f).split()[0]) # read first line
    for line in f: # read rest of lines
        array.append([int(x) for x in line.split()][0])


print("numCases: " + str(numCases))
print(array)

RE_0 = re.compile('0')
RE_1 = re.compile('1')
RE_2 = re.compile('2')
RE_3 = re.compile('3')
RE_4 = re.compile('4')
RE_5 = re.compile('5')
RE_6 = re.compile('6')
RE_7 = re.compile('7')
RE_8 = re.compile('8')
RE_9 = re.compile('9')

def has(digit, string):
    if digit == 0:
         return 1 if RE_0.search(string) else 0
    if digit == 1:
        return 1 if RE_1.search(string) else 0
    if digit == 2:
        return 1 if RE_2.search(string) else 0
    if digit == 3:
        return 1 if RE_3.search(string) else 0
    if digit == 4:
        return 1 if RE_4.search(string) else 0
    if digit == 5:
        return 1 if RE_5.search(string) else 0
    if digit == 6:
        return 1 if RE_6.search(string) else 0
    if digit == 7:
        return 1 if RE_7.search(string) else 0
    if digit == 8:
        return 1 if RE_8.search(string) else 0
    if digit == 9:
        return 1 if RE_9.search(string) else 0
    
def findSleepNumber(n):
    if n == 0:
        return "INSOMNIA"
    '''
    magnitude = 0
    
    while(n%10 == 0):
        magnitude += 1
        n //= 10
    '''
        
    multiplier = 1

    hasSeenDigit = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while(sum(hasSeenDigit)<10): #and n*multiplier < sys.maxsize):
        temp = str(n*multiplier)
        for digit in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            hasSeenDigit[digit] = 1 if has(digit, temp) else hasSeenDigit[digit]
        multiplier += 1

    return n*(multiplier-1)#*(10**magnitude)

with open('output.txt', 'w') as out:
    for index, value in enumerate(array):
        print(str("Case #" + str(index+1) + ": " + str(findSleepNumber(value))))
        out.write(str("Case #" + str(index+1) + ": " + str(findSleepNumber(value))) + '\n')
