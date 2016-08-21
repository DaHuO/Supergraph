import sys

def solve(n):
    i = 0
    while '-' in n:
        index = n.rfind('-')
        n = "".join(['+' if x == '-' else '-' for x in n[:index + 1]]) + n[index + 1:]
        i += 1
    return i

def output(result):
    with open("output1.txt", 'w') as f:
        for i, j in result:
            f.write("Case #" + str(i + 1) + ": " + str(j) + "\n")

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        t = int(f.readline())
        result = []
        for case in xrange(t):
            result.append((case, solve(f.readline())))
        output(result)