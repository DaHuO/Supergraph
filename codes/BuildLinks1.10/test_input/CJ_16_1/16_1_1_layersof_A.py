def main():
    N = input()
    for i in range(N):
        print 'Case #%d: %s' % (i+1, solve())

def solve():
    S = raw_input()
    buf = S[0]
    for c in S[1:]:
        # print '#', c, buf[-1], ord(c),ord(buf[-1]), ord(c) > ord(buf[-1])
        if ord(c) >= ord(buf[0]):
            buf = c + buf
        else:
            buf = buf + c

    return buf












if __name__ == '__main__':
    main()
