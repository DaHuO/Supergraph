
import sys

def main():
    data = sys.stdin.readlines()
    for i in range(1, len(data)):
        print("Case #" + str(i) + ": " + str(solve(data[i])))

def solve(stack):
    if '-' not in stack:
        return 0
    first = stack[0]
    found = False
    for i in range(len(stack)):
        if stack[i]!=first:
            n = i
            found = True
            break
    if not found:
        n = len(stack)
    stack = flip(stack, n)
    return solve(stack) + 1

def flip(stack, n):
    if '+' not in stack:
        return '+' * len(stack)
    for i in range(n):
        choose = '-' if stack[i] == '+' else '+'
        stack = stack[:i] + choose + stack[i+1:]
    return stack


if __name__ == '__main__':
    main()

