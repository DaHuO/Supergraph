import numpy as np
import scipy
from scipy import optimize

words = ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE")

EPS = 1e-5

def solve(s):
    y = [0] * 26
    for c in s:
        code = ord(c) - ord('A')
        y[code] += 1
    matrix = []
    #print(y)
    for c in xrange(26):
        char = chr(ord('A') + c)
        ar = [w.count(char) for w in words]
        matrix.append(ar)
    x = scipy.optimize.nnls(matrix, y)[0]
    result = ""
    i = 0
    for amo in x:
        if amo < EPS:
            v = 0
        else:
            v = int(round(amo))

        result += str(i) * v
        i += 1
    return result


def main():
    T = int(input())
    for t in xrange(T):
        s = raw_input()
        result = solve(s)
        print('Case #%s: %s' % (t+1, result))

if __name__ == "__main__":
    main()
