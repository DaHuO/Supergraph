def solve(stack):
    n = 0
    i = 0
    length = len(stack)
    while i < length:
        if stack[i] == 0:
            if i == 0:
                n += 1
            else:
                n += 2
            while i < length and stack[i] == 0:
                i += 1
        else:
            i += 1
    return n

def main():
    T = int(raw_input())
    for i in range(1, T+1):
        raw = raw_input()
        stack = []
        for c in raw:
            if c == '+':
                stack.append(1)
            else:
                stack.append(0)
        num = solve(stack)
        print 'Case #%d: %d' % (i, num)

if __name__ == '__main__':
    main()
