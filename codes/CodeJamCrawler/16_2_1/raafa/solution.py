#!/usr/bin/python

from collections import defaultdict
import sys

def solve(string):
    freq = defaultdict(int)
    
    for ch in string:
        freq[ch] += 1
    
    digits = []
    
    for ch, digit, word in [
        ('Z', 0, 'ZERO'),
        ('W', 2, 'TWO'),
        ('U', 4, 'FOUR'),
        ('X', 6, 'SIX'),
        ('G', 8, 'EIGHT'),
        ('T', 3, 'THREE'),
        ('F', 5, 'FIVE'),
        ('O', 1, 'ONE'),
        ('V', 7, 'SEVEN'),
        ('N', 9, 'NINE'),
    ]:
        n = min( freq[ch] for ch in word )
        if n > 0:
            digits.extend([digit] * n)
            for c in word:
                freq[c] -= n
        
    return ''.join(map(str, sorted(digits)))


lines = sys.stdin.readlines()
T = int(lines[0])

for i, ln in enumerate(lines[1:]):
    print 'Case #%d: %s' % (i+1, solve(ln.strip()))
