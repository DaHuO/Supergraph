#!/c/Python27/python

import sys
import copy

digits = {
        'ZERO': '0',
        'ONE': '1',
        'TWO': '2',
        'THREE': '3',
        'FOUR': '4',
        'FIVE': '5',
        'SIX': '6',
        'SEVEN': '7',
        'EIGHT': '8',
        'NINE': '9',
}
next_digits = {
        'ZERO': 'ONE',
        'ONE': 'TWO',
        'TWO': 'THREE',
        'THREE': 'FOUR',
        'FOUR': 'FIVE',
        'FIVE': 'SIX',
        'SIX': 'SEVEN',
        'SEVEN': 'EIGHT',
        'EIGHT': 'NINE',
        'NINE': '',
}

def find_number(counts, digit = 'ZERO'):
    deducted = {}
    for c in digit:
        if c in deducted:
            deducted[c] += 1
        else:
            deducted[c] = 1

    for i in xrange(667):
        done = False
        for c in deducted:
            if c not in counts or counts[c] - (deducted[c] * (i + 1)) < 0:
                done = True
                break
        if done:
            break

    for j in xrange(i + 1):
        if j != 0:
            for c in deducted:
                counts[c] -= deducted[c] * j
        done = True
        for c in counts: 
            if counts[c] != 0:
                done = False
        if done:
            if j != 0:
                return digits[digit] * j
            else:
                return ''
        else:
            if next_digits[digit]:
                ret = find_number(counts, digit = next_digits[digit])
            else:
                ret = ''
            done = True
            for c in counts: 
                if counts[c] != 0:
                    done = False
            if done:
                if j != 0:
                    return digits[digit] * j + ret
                else:
                    return ret
            if j != 0:
                for c in deducted:
                    counts[c] += deducted[c] * j

def calc(s):
    counts = {}
    for c in s:
        if c in counts:
            counts[c] += 1
        else:    
            counts[c] = 1
    return find_number(counts)



def main():
    N = int(sys.stdin.readline())
    ss = []
    for i in range(N):
        s = sys.stdin.readline()[:-1]
        print 'Case #%d: %s' % (i + 1, calc(s))

if __name__ == '__main__':
    main()
