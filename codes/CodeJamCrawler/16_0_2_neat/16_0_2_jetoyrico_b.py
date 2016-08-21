INPUT_FILE_NAME = 'B-large.in'
OUTPUT_FILE_NAME = 'out'

fin = open(INPUT_FILE_NAME)
fout = open(OUTPUT_FILE_NAME, 'w')

def ok(str):
    for c in str:
        if c == '-':
            return False
    return True

def flip(str):
    res = ''
    for c in str:
        if c == '-':
            res += '+'
        else:
            res += '-'
    return res

def f(str):
    n = 0
    while not ok(str):
        n += 1
        for i in reversed(xrange(len(str))):
            if str[i] == '-':
                str = flip(str[0:i + 1]) + str[i + 1:]
                break
    return n

for case in xrange(1, 1 + int(fin.readline())):
    s = fin.readline()
    fout.write("Case #%d: %s\n" % (case, str(f(s))))

fout.close()
fin.close()
