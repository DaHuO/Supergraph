import fileinput

def removeChar(line, ch):
    pos = line.find(ch)
    result = line[0:pos]
    if len(line) >= pos + 1:
        result = line[0:pos] + line[pos+1:]
#    print "%s -> %s" % (line, result)
    return result
    

def convert(line):
    num = []
    while 'Z' in line:
        line = removeChar(line, 'Z')
        line = removeChar(line, 'E')
        line = removeChar(line, 'R')
        line = removeChar(line, 'O')
        num.append(0)
    while 'W' in line:
        line = removeChar(line, 'T')
        line = removeChar(line, 'W')
        line = removeChar(line, 'O')
        num.append(2)
    while 'U' in line:
        line = removeChar(line, 'F')
        line = removeChar(line, 'O')
        line = removeChar(line, 'U')
        line = removeChar(line, 'R')
        num.append(4)
    while 'R' in line:
        line = removeChar(line, 'T')
        line = removeChar(line, 'H')
        line = removeChar(line, 'R')
        line = removeChar(line, 'E')
        line = removeChar(line, 'E')
        num.append(3)
    while 'F' in line:
        line = removeChar(line, 'F')
        line = removeChar(line, 'I')
        line = removeChar(line, 'V')
        line = removeChar(line, 'E')
        num.append(5)
    while 'X' in line:
        line = removeChar(line, 'S')
        line = removeChar(line, 'I')
        line = removeChar(line, 'X')
        num.append(6)
    while 'S' in line:
        line = removeChar(line, 'S')
        line = removeChar(line, 'E')
        line = removeChar(line, 'V')
        line = removeChar(line, 'E')
        line = removeChar(line, 'N')
        num.append(7)
    while 'H' in line:
        line = removeChar(line, 'E')
        line = removeChar(line, 'I')
        line = removeChar(line, 'G')
        line = removeChar(line, 'H')
        line = removeChar(line, 'T')
        num.append(8)
    while 'I' in line:
        line = removeChar(line, 'N')
        line = removeChar(line, 'I')
        line = removeChar(line, 'N')
        line = removeChar(line, 'E')
        num.append(9)
    while 'N' in line:
        line = removeChar(line, 'O')
        line = removeChar(line, 'N')
        line = removeChar(line, 'E')
        num.append(1)
    return "".join(map(lambda x : str(x), sorted(num)))

def main():
    testcases = int(raw_input()) 
    for case in xrange(testcases):
        line = raw_input()
        print "Case #%d: %s" % (case + 1, convert(line))

if __name__ == "__main__":
    main()
