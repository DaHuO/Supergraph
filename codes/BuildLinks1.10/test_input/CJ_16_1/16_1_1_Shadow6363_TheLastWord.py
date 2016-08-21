import sys


def main():
    T = int(sys.stdin.readline().strip())
    for case in xrange(T):
        s = list(sys.stdin.readline().strip())
        word = []

        for letter in s:
            if word:
                if letter >= word[0]:
                    word.insert(0, letter)
                else:
                    word.append(letter)
            else:
                word.append(letter)

        print 'Case #{0}: {1}'.format(case+1, ''.join(word))


if __name__ == '__main__':
    main()
