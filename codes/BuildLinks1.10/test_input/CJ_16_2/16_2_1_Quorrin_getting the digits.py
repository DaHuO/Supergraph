f = open('input1.in', 'r')
n = int(f.readline().strip())
out = open('output1.txt', 'w')


"""
Z E R O - Z
O N E
T W O - W
T H R E E -
F O U R - U
F I V E - F!U
S I X - X
S E V E N - V!F
E I G H T - G
N I N E - 

"""

def containsZero(s):
    return ('Z' in s or 'z' in s)

def removeZero(cArr, s):
    if (containsZero(s)):
        s.remove('Z')
        s.remove('E')
        s.remove('R')
        s.remove('O')
        cArr.append(0)
        return cArr, s
    else:
        return cArr, s

def containsTwo(s):
    return ('W' in s or 'w' in s)

def removeTwo(cArr, s):
    if (containsTwo(s)):
        s.remove('T')
        s.remove('W')
        s.remove('O')
        cArr.append(2)
        return cArr, s
    else:
        return cArr, s

def containsFour(s):
    return ('U' in s or 'u' in s)

def removeFour(cArr, s):
    if (containsFour(s)):
        s.remove('F')
        s.remove('O')
        s.remove('U')
        s.remove('R')
        cArr.append(4)
        return cArr, s
    else:
        return cArr, s

def containsSix(s):
    return ('X' in s or 'x' in s)

def removeSix(cArr, s):
    if (containsSix(s)):
        s.remove('S')
        s.remove('I')
        s.remove('X')
        cArr.append(6)
        return cArr, s
    else:
        return cArr, s

def containsEight(s):
    return ('G' in s or 'g' in s)

def removeEight(cArr, s):
    if (containsEight(s)):
        s.remove('E')
        s.remove('I')
        s.remove('G')
        s.remove('H')
        s.remove('T')
        cArr.append(8)
        return cArr, s
    else:
        return cArr, s
"""
Non uniques

"""

def containsThree(s):
    return ('R' in s or 'r' in s)

def removeThree(cArr, s):
    if (containsThree(s)):
        s.remove('T')
        s.remove('H')
        s.remove('R')
        s.remove('E')
        s.remove('E')
        cArr.append(3)
        return cArr, s
    else:
        return cArr, s


def containsFive(s):
    return ('F' in s or 'f' in s)

def removeFive(cArr, s):
    if (containsFive(s)):
        s.remove('F')
        s.remove('I')
        s.remove('V')
        s.remove('E')
        cArr.append(5)
        return cArr, s
    else:
        return cArr, s



def containsSeven(s):
    return ('V' in s or 'v' in s)

def removeSeven(cArr, s):
    if (containsSeven(s)):
        s.remove('S')
        s.remove('E')
        s.remove('V')
        s.remove('E')
        s.remove('N')
        cArr.append(7)
        return cArr, s
    else:
        return cArr, s


def containsOne(s):
    return ('O' in s or 'o' in s)

def removeOne(cArr, s):
    if (containsOne(s)):
        s.remove('O')
        s.remove('N')
        s.remove('E')
        cArr.append(1)
        return cArr, s
    else:
        return cArr, s



def containsNine(s):
    return ('N' in s or 'n' in s)

def removeNine(cArr, s):
    if (containsNine(s)):
        s.remove('N')
        s.remove('I')
        s.remove('N')
        s.remove('E')
        cArr.append(9)
        return cArr, s
    else:
        return cArr, s



def getNumbers(re):
    num = []
    while(containsZero(re)):
        num, re = removeZero(num,re)
    while(containsTwo(re)):
        num, re = removeTwo(num, re)
    while(containsFour(re)):
        num, re = removeFour(num, re)
    while(containsSix(re)):
        num, re = removeSix(num, re)
    while(containsEight(re)):
        num, re = removeEight(num, re)
    while(containsThree(re)):
        num, re = removeThree(num, re)
    while(containsFive(re)):
        num, re = removeFive(num, re)
    while(containsSeven(re)):
        num, re = removeSeven(num, re)
    while(containsOne(re)):
        num, re = removeOne(num, re)
    while(containsNine(re)):
        num, re = removeNine(num, re)
    return num, re

for i in range(n):
    inputStr = f.readline().strip()
    arr = list(inputStr)
    num, remaining = getNumbers(arr)
    num.sort()
    num = ''.join(list(map(str,num)))
    print(num)
    print (remaining)
    out.write("Case #" + str(i+1) + ": " + num + "\n")
        


out.close()
f.close()


