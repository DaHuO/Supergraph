# coding: UTF8


def lastword(word):
    words = []
    words = [word[0]]
    for s in word[1:]:
        new_words = []
        for w in words:
            if s+w > w+s:
                new_words.append(s + w)
            else:
                new_words.append(w + s)
        words = new_words
    words = sorted(words)
    return words[-1]


def counter(t, n):
    for i in xrange(t):
        print('Case #{}: {}'.format(i+1, lastword(n[i])))


def main():
    tests = int(raw_input())
    cases = []
    for i in xrange(tests):
        cases.append(raw_input())
    # print tests, cases
    counter(tests, cases)


if __name__ == '__main__':
    main()
