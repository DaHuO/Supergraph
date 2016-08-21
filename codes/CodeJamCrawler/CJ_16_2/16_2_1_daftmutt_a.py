import sys

fi = open('A-large.in', 'r')
fo = open('a.out', 'w')

T = int(fi.readline())

letters = 'ZWUXGOTFVE'
written = ['ZERO', 'TWO', 'FOUR', 'SIX', 'EIGHT', 'ONE', 'THREE', 'FIVE',
        'SEVEN', 'NINE']
numbers = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]

for t in xrange(T):
    # solve
    S = fi.readline()
    l_counts = {}

    answer = ''
    for l in letters:
        l_counts[l] = 0
    for c in S:
        if c in letters:
            l_counts[c] += 1

    print l_counts
    for i, l in enumerate(letters):
        count = l_counts[l]
        answer += count * str(numbers[i])
        for c in written[i]:
            if c in l_counts and l_counts[c] > 0:
                l_counts[c] -= count
    print S
    print l_counts
    answer = ''.join(sorted(answer)) 

    fo.write('Case #{}: {}\n'.format(t + 1, answer))
    print 'Case #{}: {}'.format(t + 1, answer)

fi.close()
fo.close()

