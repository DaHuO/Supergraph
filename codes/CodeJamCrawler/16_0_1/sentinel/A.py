import sys

def findMatch(num, numbers):
    firstNum = str(num)
    remainArr = [x for x in numbers]
    numArr = [x for x in firstNum]

    ret = [x for x in remainArr if x not in numArr]
    return "".join(ret)

def processRecord(fp):
    num = int(fp.readline())
    numbers = "0123456789"
    if num == 0:
        return "INSOMNIA"
    n = 0
    while len(numbers) > 0:
        n = n + 1
        numbers = findMatch(n*num, numbers)
    return n*num

def processLine(fp, x):
    result = processRecord(fp)
    print 'Case #{}: {}'.format(x, result)

def main():
    filename = sys.argv[1]

    try:
        fp = open(filename)
        records = int(fp.readline())
        for x in xrange(records):
            processLine(fp, x+1)
        fp.close()
    except Exception as e:
        print e

if __name__ == '__main__':
    main()
