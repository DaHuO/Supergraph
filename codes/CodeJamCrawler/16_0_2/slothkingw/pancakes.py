import sys

def flip(stack, i):
    flipped = ''
    for c in reversed(stack[:i]):
        if c == '+':
            c = '-'
        else:
            c = '+'
        flipped += c

    flipped += stack[i:]

    return flipped

def count_flips(stack):
    count=0
    cnow=stack[0]
    for c in stack:
        if c != cnow:
            count += 1
            cnow = c

    if cnow == '-':
        count += 1

    return count

def main():
    N = int(raw_input())
    for i in range(1, N+1):
        line = sys.stdin.readline()[:-1]
        print 'Case #%d: %d' % (i, count_flips(line))

if __name__ == '__main__':
    main()
