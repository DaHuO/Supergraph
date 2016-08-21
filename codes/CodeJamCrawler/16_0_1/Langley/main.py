import sys
from sets import Set

def extract(result):
    return list(str(result))

def finished(results):
    # print results
    if len(results) >= 10:
        return True
    else:
        return False

def calculate(value):
    result = Set([])

    p = 1
    previous_result = -1
    while not finished(result):
        tem = p * value
        # print tem, p, value

        ext = extract(tem)
        for x in ext:
            result.add(x)

        p += 1

        if previous_result == tem:
            return 'INSOMNIA'
        else:
            previous_result = tem

    return tem

def go():
    filename = sys.argv[1]

    with open(filename) as f:
        t = int(f.readline().strip())

        for x in range(1, t+1):
            value = int(f.readline().strip())
            print 'Case #%d: %s' % (x, calculate(value))

go()
