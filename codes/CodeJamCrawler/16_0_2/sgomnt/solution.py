import sys


n_cases = int(sys.stdin.readline())


def reverse(word):
    for i in range(len(word)):
        if word[i] == '+':
            word = list(word)
            word[i] = '-'
            word = ''.join(word)
        elif word[i] == '-':
            word = list(word)
            word[i] = '+'
            word = ''.join(word)
    return word


def finish(cases, allplus):
    for key in cases.keys():
        if allplus in cases[key]:
                return True
    return False


def revpile(pile, cases, key):
    allplus = ''.join(['+' for i in range(len(pile))])
    while not finish(cases, allplus):
        cases[key] = []
        for string in cases[key - 1]:
            for i in range(len(string) + 1):
                new = reverse(string[0:i]) + string[i::]
                if not new in cases[key]:
                    cases[key].append(new)
        cases.pop(key - 1)
        key += 1
    return key

for i in range(n_cases):
    pile = sys.stdin.readline().strip()
    cases = {0: [pile]}
    print 'Case #' + str(i + 1) + ":", revpile(pile, cases, 1) - 1