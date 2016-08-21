import sys

T = int(sys.stdin.readline())

for t in range(T):
    S = sys.stdin.readline().strip()

    counts = {}
    for i in range(26):
        counts[chr(ord('A') + i)] = 0

    for c in S:
        counts[c] += 1

    digits = {}
    for i in range(10):
        digits[i] = 0
    
    digits[0] = counts['Z']
    counts['Z'] -= digits[0]
    counts['E'] -= digits[0]
    counts['R'] -= digits[0]
    counts['O'] -= digits[0]

    digits[6] = counts['X']
    counts['S'] -= digits[6]
    counts['I'] -= digits[6]
    counts['X'] -= digits[6]

    digits[2] = counts['W']
    counts['T'] -= digits[2]
    counts['W'] -= digits[2]
    counts['O'] -= digits[2]

    digits[8] = counts['G']
    counts['E'] -= digits[8]
    counts['I'] -= digits[8]
    counts['G'] -= digits[8]
    counts['H'] -= digits[8]
    counts['T'] -= digits[8]

    digits[4] = counts['U']
    counts['F'] -= digits[4]
    counts['O'] -= digits[4]
    counts['U'] -= digits[4]
    counts['R'] -= digits[4]

    digits[1] = counts['O']
    counts['O'] -= digits[1]
    counts['N'] -= digits[1]
    counts['E'] -= digits[1]

    digits[7] = counts['S']
    counts['S'] -= digits[7]
    counts['E'] -= digits[7]
    counts['V'] -= digits[7]
    counts['E'] -= digits[7]
    counts['N'] -= digits[7]

    digits[5] = counts['V']
    counts['F'] -= digits[5]
    counts['I'] -= digits[5]
    counts['V'] -= digits[5]
    counts['E'] -= digits[5]

    digits[3] = counts['T']
    counts['T'] -= digits[3]
    counts['H'] -= digits[3]
    counts['R'] -= digits[3]
    counts['E'] -= digits[3]
    counts['E'] -= digits[3]

    digits[9] = counts['E']
    counts['N'] -= digits[9]
    counts['I'] -= digits[9]
    counts['N'] -= digits[9]
    counts['E'] -= digits[9]

    print("Case #{}: ".format(t+1), end='')

    for d in range(10):
        print(str(d) * digits[d], end='')

    print()


