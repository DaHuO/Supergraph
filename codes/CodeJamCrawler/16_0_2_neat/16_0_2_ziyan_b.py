import os
import sys

def neg(s):
    return '+' if s == '-' else '-'

def rev(S):
    return ''.join(map(neg, reversed(S)))

def solve2(S):
    count = 0
    S = S.rstrip('+')
    while S:
        if S[0] == '-':
            S = rev(S)
        else:
            S1 = rev(S.rstrip('-'))
            S = S1 + S[len(S1):]
        S = S.rstrip('+')
        count += 1
    return count

def solve(S):
    goal = '+' * len(S)
    queue = [(S, 0)]
    seen = set()
    while queue:
        stack, flips = queue.pop(0)
        if stack == goal:
            return flips
        for i in range(len(stack.lstrip('+'))):
            newstack = ''.join([
                '+' if s == '-' else '-'
                for s in reversed(stack[0:i + 1])
            ]) + stack[i + 1:]
            if newstack in seen:
                continue
            seen.add(newstack)
            queue.append((newstack, flips + 1))
    return 0

def main():
    T = int(sys.stdin.readline().strip())
    for t in range(T):
        S = sys.stdin.readline().strip()
        result = solve2(S)
        print 'Case #%d: %d' % (t + 1, result)

if __name__ == '__main__':
    main()

