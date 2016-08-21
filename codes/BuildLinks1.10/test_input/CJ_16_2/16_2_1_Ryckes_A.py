
cases = int(raw_input())

for case in xrange(cases):
    counts = [0] * 10
    letterCounts = {}
    letters = 'abcdefghijklmnopqrstuvwxyz'.upper()
    for letter in letters:
        letterCounts[letter] = 0

    inputstr = raw_input()
    for letter in inputstr:
        letterCounts[letter] += 1

    def accountFor(num, word, definingLetter):
        global counts

        counts[num] += letterCounts[definingLetter]
        for letter in word:
            letterCounts[letter] -= counts[num]

    accountFor(4, 'FOUR', 'U')
    accountFor(6, 'SIX', 'X')
    accountFor(0, 'ZERO', 'Z')
    accountFor(8, 'EIGHT', 'G')
    accountFor(2, 'TWO', 'W')

    # After removing 4s and 0s
    accountFor(3, 'THREE', 'R')

    # After removing 4s
    accountFor(5, 'FIVE', 'F')

    # After removing 5s
    accountFor(7, 'SEVEN', 'V')

    # After all the others, only NINE and ONE remain
    accountFor(9, 'NINE', 'I')
    accountFor(1, 'ONE', 'O')

    output = ''
    for num in xrange(10):
        output += str(num) * counts[num]

    print 'Case #%d: %s' % (case + 1, output)
