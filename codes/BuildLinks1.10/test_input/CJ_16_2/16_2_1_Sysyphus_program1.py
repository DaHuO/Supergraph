import sys, itertools, string

input_file_name = 'A-large.in'
output_file_name = 'outputlarge.txt'

f_in = open(input_file_name,'r')
f_out = open(output_file_name,'w')

def removezeros(l):
    i = l.count('Z')
    for j in range(i):
        l.remove('Z')
        l.remove('E')
        l.remove('R')
        l.remove('O')
    return i, l

def removeones(l):
    i = l.count('O')
    for j in range(i):
        l.remove('O')
        l.remove('N')
        l.remove('E')
    return i, l

def removetwos(l):
    i = l.count('W')
    for j in range(i):
        l.remove('T')
        l.remove('W')
        l.remove('O')
    return i, l

def removethrees(l):
    i = l.count('R')
    for j in range(i):
        l.remove('T')
        l.remove('H')
        l.remove('R')
        l.remove('E')
        l.remove('E')
    return i, l

def removefours(l):
    i = l.count('U')
    for j in range(i):
        l.remove('F')
        l.remove('O')
        l.remove('U')
        l.remove('R')
    return i, l

def removefives(l):
    i = l.count('F')
    for j in range(i):
        l.remove('F')
        l.remove('I')
        l.remove('V')
        l.remove('E')
    return i, l

def removesixes(l):
    i = l.count('X')
    for j in range(i):
        l.remove('S')
        l.remove('I')
        l.remove('X')
    return i, l

def removesevens(l):
    i = l.count('V')
    for j in range(i):
        l.remove('S')
        l.remove('E')
        l.remove('V')
        l.remove('E')
        l.remove('N')
    return i, l

def removeeights(l):
    i = l.count('G')
    for j in range(i):
        l.remove('E')
        l.remove('I')
        l.remove('G')
        l.remove('H')
        l.remove('T')
    return i, l

def removenines(l):
    i = l.count('I')
    for j in range(i):
        l.remove('N')
        l.remove('I')
        l.remove('N')
        l.remove('E')
    return i, l

def convert(s):
    numlist = []
    l = list(s)

    num0, l = removezeros(l)
    for i in range(num0):
        numlist.append('0')

    num8, l = removeeights(l)
    for i in range(num8):
        numlist.append('8')
    
    num6, l = removesixes(l)
    for i in range(num6):
        numlist.append('6')

    num4, l = removefours(l)
    for i in range(num4):
        numlist.append('4')

    num5, l = removefives(l)
    for i in range(num5):
        numlist.append('5')

    num7, l = removesevens(l)
    for i in range(num7):
        numlist.append('7')

    num3, l = removethrees(l)
    for i in range(num3):
        numlist.append('3')

    num2, l = removetwos(l)
    for i in range(num2):
        numlist.append('2')

    num1, l = removeones(l)
    for i in range(num1):
        numlist.append('1')

    num9, l = removenines(l)
    for i in range(num9):
        numlist.append('9')

    return numlist

contents = f_in.readlines()
num_cases = int(contents.pop(0))

for case in range (num_cases):

    s = contents.pop(0)
    string = s.strip('\n')
    answer = convert(string)
    answer.sort()
    a = ''.join(answer)
    print('Case #{}: {}'.format(case+1, a))
    print('Case #{}: {}'.format(case+1, a), file = f_out)
  
f_in.close()
f_out.close()
