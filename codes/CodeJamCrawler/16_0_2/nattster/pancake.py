def read_int():
    return int(raw_input())


def all_plus(stack):
    for c in stack:
        if c == '-':
            return False
    return True


def all_minus(stack):
    for c in stack:
        if c == '+':
            return False
    return True


def opposite(x):
    return '+' if x == '-' else '-'


def flip(stack):
    return map(opposite, reversed(stack))


def check(stack):
    if all_plus(stack):
        return 0
    if all_minus(stack):
        return 1
    for i in range(len(stack)-1, -1, -1):
        if i > 0:
            if stack[i-1] == '+' and stack[i] == '-':
                return 2 + check(stack[0:i-1])
        if stack[i] == '-':
            return 1 + check(flip(stack[0:i]))
    return 0


def solve():
    line = raw_input()
    # merge consecutive plus & minus
    stack = ""
    lastc = ""
    for c in line:
        if c != lastc:
            stack += c
            lastc = c
    return check(stack)


def main():
    T = read_int()
    for i in range(T):
        print 'Case #%d: %s' % (i+1, solve())

if __name__ == '__main__':
    main()
