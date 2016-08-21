def read_int():
    return int(raw_input())


def solve():
    line = raw_input()
    word = line[0]
    for c in line[1:]:
        if c >= word[0]:
            word = c + word
        else:
            word = word + c
    return word


def main():
    T = read_int()
    for i in range(T):
        print 'Case #%d: %s' % (i+1, solve())

if __name__ == '__main__':
    main()
