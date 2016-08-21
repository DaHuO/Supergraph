import sys

def solve(pans):
    result = 0
    while pans.count('+') != len(pans):
        result += 1
        if pans[0] == '-':
            toSwap = pans.find('+')
            if toSwap == -1:
                toSwap = len(pans)
            pans = '+' * toSwap + pans[toSwap:]
        else:
            swapPos = pans.rfind('-')
            pans = ''.join(reversed(pans[:swapPos + 1])) + pans[swapPos + 1:]

    return result

def main(inFile):
    with open(inFile) as inp, open(inFile.replace('.in', '.out'), 'w') as out:
        T = int(inp.readline().strip())
        for t in xrange(T):
            pans = inp.readline().strip()
            out.write('Case #%d: %s\n' % (t + 1, solve(pans)))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Usage: %s input.in' % sys.argv[0])
    main(sys.argv[1])
