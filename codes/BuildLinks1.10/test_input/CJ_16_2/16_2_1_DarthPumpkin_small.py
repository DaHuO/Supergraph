import sys
from collections import Counter, defaultdict

def print_result(i, result):
    print "Case #%d: %s" % (i, result)

def solve(letter_counts):
    d = Counter()
    d[0] = letter_counts['Z']
    letter_counts.subtract('ZERO' * d[0])
    d[2] = letter_counts['W']
    letter_counts.subtract('TWO' * d[2])
    d[4] = letter_counts['U']
    letter_counts.subtract('FOUR' * d[4])
    d[6] = letter_counts['X']
    letter_counts.subtract('SIX' * d[6])
    d[8] = letter_counts['G']
    letter_counts.subtract('EIGHT' * d[8])
    
    d[1] = letter_counts['O']
    letter_counts.subtract('ONE' * d[1])
    d[3] = letter_counts['T']
    letter_counts.subtract('THREE' * d[3])
    d[5] = letter_counts['F']
    letter_counts.subtract('FIVE' * d[5])
    d[7] = letter_counts['V']
    letter_counts.subtract('SEVEN' * d[7])
    d[9] = letter_counts['I']
    letter_counts.subtract('NINE' * d[9])
    return ''.join(map(str, sorted(d.elements())))

def parse_input(case):
    letter_counts = Counter(case)
    return letter_counts

if __name__ == "__main__":
    n = int(raw_input())
    for i in range(n):
        print_result(i+1, solve(parse_input(raw_input())))
