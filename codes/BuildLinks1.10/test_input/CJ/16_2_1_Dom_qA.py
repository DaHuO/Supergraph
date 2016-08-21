import ju

results = []
FILE = "A-large"
f = ju.jopen(FILE)

def ordoff(letter):
    return ord(letter) - ord('A')

T = int(f.readline())
for t in range(T):
    letters = f.readline()[:-1]
    digits = []
    counts = [0]*26
    for letter in letters:
        counts[ord(letter)-65] += 1
    zeroes = int(counts[ordoff('Z')])
    for z in range(zeroes):
        digits += [0]
        counts[ordoff('E')] -= 1
        counts[ordoff('R')] -= 1
        counts[ordoff('O')] -= 1
    sixes = int(counts[ordoff('X')])
    for s in range(sixes):
        digits += [6]
        counts[ordoff('S')] -= 1
        counts[ordoff('I')] -= 1
    eights = int(counts[ordoff('G')])
    for e in range(eights):
        digits += [8]
        counts[ordoff('E')] -= 1
        counts[ordoff('I')] -= 1
        counts[ordoff('H')] -= 1
        counts[ordoff('T')] -= 1
    twos = int(counts[ordoff('W')])
    for t in range(twos):
        digits += [2]
        counts[ordoff('T')] -= 1
        counts[ordoff('O')] -= 1
    fours = int(counts[ordoff('U')])
    for o in range(fours):
        digits += [4]
        counts[ordoff('F')] -= 1
        counts[ordoff('O')] -= 1
        counts[ordoff('R')] -= 1
    fives = int(counts[ordoff('F')])
    for v in range(fives):
        digits += [5]
        counts[ordoff('I')] -= 1
        counts[ordoff('V')] -= 1
        counts[ordoff('E')] -= 1
    sevens = int(counts[ordoff('V')])
    for s in range(sevens):
        digits += [7]
        counts[ordoff('S')] -= 1
        counts[ordoff('E')] -= 2
        counts[ordoff('N')] -= 1
    ones = int(counts[ordoff('O')])
    for s in range(ones):
        digits += [1]
        counts[ordoff('N')] -= 1
        counts[ordoff('E')] -= 1
    threes = int(counts[ordoff('T')])
    for t in range(threes):
        digits += [3]
        counts[ordoff('T')] -= 1
        counts[ordoff('R')] -= 1
        counts[ordoff('E')] -= 2
    nines = int(counts[ordoff('N')])/2
    for n in range(nines):
        digits += [9]
        counts[ordoff('T')] -= 1
        counts[ordoff('R')] -= 1
        counts[ordoff('E')] -= 2
    digits.sort()
    print digits
    results += ["".join(map(str,digits))]







ju.jout(FILE, results)
