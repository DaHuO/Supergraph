import sys

def solve(K, C, S):
    return " ".join(str(1 + x * K**(C-1)) for x in xrange(K))

if __name__ == "__main__":
    f = open('D-small-attempt2.in', 'r')
    output = open('D-small-attempt2.out', 'w')
    C = int(f.readline())
    for i in range(0, C):
        pancakesStr = f.readline().rstrip('\n').split()
        K = int(pancakesStr[0])
        C = int(pancakesStr[1])
        S = int(pancakesStr[2])
        output.write("Case #" + str(i + 1) + ": " + str(solve(K, C, S)) + "\n")