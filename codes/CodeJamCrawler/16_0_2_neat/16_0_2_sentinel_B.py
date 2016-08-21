import sys


def flip(inStr, end):
    arr = [x for x in inStr]
    for x in xrange(end+1):
        arr[x] = '+' if arr[x] == '-' else '-'
    return "".join(arr)

def processRecord(inStr):
    n = 0
    while '-' in inStr:
        n = n+1
        end = inStr.rfind('-')
        # start = end
        # while start >= 1 and arr[start-1] == '-':
        #     start = start -1
        inStr = flip(inStr, end)

    return n


def processLine(fp, x):
    result = processRecord(fp.readline())
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
        raise e

if __name__ == '__main__':
    main()
