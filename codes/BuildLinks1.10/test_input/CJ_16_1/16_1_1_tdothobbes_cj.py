import fileinput

from collections import defaultdict

def last_word(S):
    words_by_size = defaultdict(list)
    s = 1
    for c in S:
        if s == 1:
            words_by_size[1] = [c]
        else:
            for x in words_by_size[s-1]:
                words_by_size[s].append(c + x)
                words_by_size[s].append(x + c)
        s += 1
    return sorted(words_by_size[len(S)])[-1]


if __name__ == '__main__':
    i = 0
    for line in fileinput.input():
        if i > 0:
            print('Case #{}: {}'.format(i, last_word(line.strip())))
        i += 1

