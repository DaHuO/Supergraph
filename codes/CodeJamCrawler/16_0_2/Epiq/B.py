import re

def solve():
    s = raw_input().strip()
    s += '+'
    s = re.sub('[+]+', '+', s)
    s = re.sub('[-]+', '-', s)
    
    return len(s) - 1

def main():
    T = int(raw_input())
    
    for t in range(1, T + 1):
        print 'Case #%d:' % t, solve()


if __name__ == '__main__':
    main()