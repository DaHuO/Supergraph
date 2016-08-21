
import sys
sys.setrecursionlimit(5000)

def last_word(s):
    # n is maximum. solution is
    # s[n] + last_word(s[:n-1]) + s[n+1:]

    if len(s) <= 1:
        return s

    n = len(s) - s[::-1].index(max(s)) - 1

    if n == 0:
        return s

    return s[n] + last_word(s[:n]) + s[n+1:]

def main():
    n = int(sys.stdin.readline().strip())
    for k in range(n):
        line = sys.stdin.readline().strip()
        solution = last_word(line)
        print 'Case #' + str(k+1) + ': ' + solution

if __name__ == '__main__':
    main()

