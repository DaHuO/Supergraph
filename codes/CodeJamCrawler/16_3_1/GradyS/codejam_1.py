def readfile(filename):
    textfile = open(filename, 'r')
    text = ''
    while True:
        read = textfile.readline()
        if not read:
            break
        text += read
    return text

def writefile(filename, text):
    textfile = open(filename, 'w')
    textfile.write(text)
    textfile.close()

def sequence(case):
    result = []
    while [not i for i in case] != [True] * len(case): # all zeros
        highest = max(case)
        maximums = [i for i, x in enumerate(case) if x == highest]
        if len(maximums) >= 2:
            result.append(chr(65+maximums[0]) + chr(65+maximums[1]))
            case[maximums[0]] -= 1
            case[maximums[1]] -= 1
        else:
            result.append(chr(65+maximums[0]))
            case[maximums[0]] -= 1
    return ' '.join(result)

def fix(result):
    if len(result) >= 4 and result[-2] == ' ':
        return result[:-3] + ' ' + result[-3] + result[-1]
    else:
        return result

cases = [[int(val) for val in case.split(' ')] for case in readfile("A-large.in").split('\n')[2::2] if case != '']
output = ''

for case in range(len(cases)):
    output += 'Case #' + str(case+1) + ': ' + fix(sequence(cases[case])) + ('\n' if case != len(cases)-1 else '')

writefile("output.txt", output)
