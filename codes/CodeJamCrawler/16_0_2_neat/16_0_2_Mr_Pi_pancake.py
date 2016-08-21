import sys

def trim(line):
    endptr = len(line) - 1
    while line[endptr] == '+':
        endptr -= 1
        if endptr < 0: return ""
    return line[:endptr+1]

def flip(line):
    return "".join(['+' if x == '-' else '-' for x in reversed(line)])

def pancake(line):
    ans = 0
    if len(line) > 0:
        line = trim(line)
    if len(line) > 0 and line[0] == '-':
        line = trim(flip(line))
        ans += 1
    while len(line) > 0:
        startptr = 0
        while line[startptr] == '+':
            startptr += 1
        line = flip(line[:startptr])+line[startptr:]
        line = trim(flip(line))
        ans += 2
    return ans

if __name__ == "__main__":
    f = open(sys.argv[1])
    T = int(f.readline().strip())
    for i in xrange(1, T+1):
        line = f.readline().strip()
        ans = pancake(line)

        """
        val = [True for x in line if x == '+' else False]
        ans = 0
        end_idx = len(val) - 1
        while end_idx >= 0:        
        """
        print("Case #"+str(i)+": "+str(ans))
    f.close()
