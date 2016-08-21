fin = open('B-large.in', 'r')
fout = open('output.txt', 'w')

t = int(fin.readline())

def cutOff(s):
    string = s[::-1]
    pluses = 0
    for i in string:
        if i == '+':
            pluses += 1
        else:
            break
    if pluses > 0:
        return s[0:-pluses]
    else:
        return s

def inverse(s):
    string = ''
    for i in s:
        if i == '+':
            string += '-'
        else:
            string += '+'
    return string

def trim(s):
    string = ''
    for i in s:
        if i == '+' or i == '-':
            string += i
    return string

for i in xrange(t):
    s = fin.readline()
    s = trim(s)
    s = cutOff(s)
    answer = 0
    while len(s) > 0:
        s = inverse(s)
        s = cutOff(s)
        answer += 1
    fout.write('Case #' + str(i + 1) + ': ' + str(answer) + '\n')

fout.close()

print 'FINISHED'
