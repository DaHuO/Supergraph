t = int(raw_input())
finalString = ''

def removeChar(string , pos):
    return string[0:pos]+string[pos+1:]

def findZero():
    global string
    global finalString
    if 'Z' in string :
        # string.replace('Z','').replcae
        pos = string.index('Z')
        string  = removeChar(string,pos)
        pos = string.index('E')
        string  = removeChar(string,pos)
        pos = string.index('R')
        string  = removeChar(string,pos)
        pos = string.index('O')
        string = removeChar(string,pos)
        finalString = finalString+'0'
        # print finalString
        # print string
        findZero()
    else:
        return

def findOne():
    global finalString
    global string

    if 'O' in string and 'N' in string:
        pos = string.index('O')
        string  = removeChar(string,pos)
        pos = string.index('N')
        string  = removeChar(string,pos)
        pos = string.index('E')
        string = removeChar(string,pos)
        finalString = finalString+'1'
        findOne()
    else:
        return

def findTwo():
    global finalString
    global string

    if 'W' in string and 'O' in string:
        pos = string.index('T')
        string  = removeChar(string,pos)
        pos = string.index('W')
        string  = removeChar(string,pos)
        pos = string.index('O')
        string = removeChar(string,pos)
        finalString = finalString+'2'
        findTwo()
    else:
        return

def findThree():
    global finalString
    global string

    if 'T' in string and 'H' in string and 'R' in string and string.count('E')>=2:
        pos = string.index('T')
        string  = removeChar(string,pos)
        pos = string.index('H')
        string  = removeChar(string,pos)
        pos = string.index('R')
        string = removeChar(string,pos)
        pos = string.index('E')
        string = removeChar(string,pos)
        pos = string.index('E')
        string = removeChar(string,pos)
        finalString = finalString+'3'
        findThree()
    else:
        return

def findFour():
    global finalString
    global string

    if 'U' in string and 'O' in string:
        pos = string.index('F')
        string  = removeChar(string,pos)
        pos = string.index('O')
        string  = removeChar(string,pos)
        pos = string.index('U')
        string = removeChar(string,pos)
        pos = string.index('R')
        string = removeChar(string,pos)
        finalString = finalString+'4'
        findFour()
    else:
        return

def findFive():
    global finalString
    global string

    if 'I' in string and 'V' in string and 'F' in string and 'E' in string:
        pos = string.index('F')
        string  = removeChar(string,pos)
        pos = string.index('I')
        string  = removeChar(string,pos)
        pos = string.index('V')
        string = removeChar(string,pos)
        pos = string.index('E')
        string = removeChar(string,pos)
        finalString = finalString+'5'
        findFive()
    else:
        return

def findSix():
    global finalString
    global string

    if 'X' in string and 'I' in string:
        pos = string.index('S')
        string  = removeChar(string,pos)
        pos = string.index('I')
        string  = removeChar(string,pos)
        pos = string.index('X')
        string  = removeChar(string,pos)
        finalString = finalString +'6'
        findSix()
    else:
        return


def findSeven():
    global finalString
    global string

    if 'S' in string and 'V' in string and string.count('E')>=2:
        pos = string.index('S')
        string  = removeChar(string,pos)
        pos = string.index('E')
        string  = removeChar(string,pos)
        pos = string.index('V')
        string  = removeChar(string,pos)
        pos = string.index('E')
        string  = removeChar(string,pos)
        pos = string.index('N')
        string  = removeChar(string,pos)
        finalString = finalString +'7'
        findSeven()
    else:
        return

def findEight():
    global finalString
    global string

    if 'G' in string :
        pos = string.index('E')
        string  = removeChar(string,pos)
        pos = string.index('I')
        string  = removeChar(string,pos)
        pos = string.index('G')
        string  = removeChar(string,pos)
        pos = string.index('H')
        string  = removeChar(string,pos)
        pos = string.index('T')
        string  = removeChar(string,pos)
        finalString = finalString +'8'
        findEight()
    else:
        return

def findNine():
    global finalString
    global string

    if 'I' in string and string.count('N')>=2:
        pos = string.index('N')
        string  = removeChar(string,pos)
        pos = string.index('I')
        string  = removeChar(string,pos)
        pos = string.index('N')
        string  = removeChar(string,pos)
        pos = string.index('E')
        finalString = finalString + '9'
        findNine()
    else:
        return



string = ''
for i in xrange(t):

    finalString = ''
    string = raw_input()
    # print string
    if len(string)>0:
        findZero()
    if len(string)>0:
        findSix()
    if len(string)>0:
        findTwo()
    if len(string)>0:
        findFive()
    if len(string)>0:
        findEight()
    if len(string)>0:
        findFour()
    if len(string)>0:
        findSeven()
    if len(string)>0:
        findThree()
    if len(string)>0:
        findOne()
    if len(string)>0:
        findNine()
    last = list(finalString)
    last.sort()
    finalString = ''.join(last)
    print 'Case #'+str(i+1)+': '+finalString
