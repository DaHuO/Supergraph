T = int(raw_input())

def solve(letters):
    word = letters[0]
    for letter in letters[1:]:
        if letter >= word[0]:
            word = letter + word
        else:
            word = word + letter
    return word
for t in range(1, T + 1):
    word = raw_input()
    print 'Case #%d: %s' % (t, solve(list(word)))
