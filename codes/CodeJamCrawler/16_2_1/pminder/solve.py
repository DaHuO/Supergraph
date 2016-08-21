numbers = [
        "ZERO",
        "ONE",
        "TWO",
        "THREE",
        "FOUR",
        "FIVE",
        "SIX",
        "SEVEN",
        "EIGHT",
        "NINE"
        ]

def countWords(s):

    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1

    return d

def solve():
    line = raw_input()

    counts = countWords(line)

    nZeros = counts.get("Z", 0)
    for c in "ZERO":
        counts[c] = counts.get(c, 0) - nZeros

    nSixs = counts.get("X", 0)
    for c in "SIX":
        counts[c] = counts.get(c, 0) - nSixs

    nTwos = counts.get("W", 0)
    for c in "TWO":
        counts[c] = counts.get(c, 0) - nTwos

    nEights = counts.get("G", 0)
    for c in "EIGHT":
        counts[c] = counts.get(c, 0) - nEights

    nThrees = counts.get("H", 0)
    for c in "THREE":
        counts[c] = counts.get(c, 0) - nThrees
    
    nFours = counts.get("R", 0)
    for c in "FOUR":
        counts[c] = counts.get(c, 0) - nFours

    nOnes = counts.get("O", 0)
    for c in "ONE":
        counts[c] = counts.get(c, 0) - nOnes

    nFives = counts.get("F", 0)
    for c in "FIVE":
        counts[c] = counts.get(c, 0) - nFives

    nSeven = counts.get("V", 0)
    for c in "SEVEN":
        counts[c] = counts.get(c, 0) - nSeven

    nNine = counts.get("I", 0)
    for c in "NINE":
        counts[c] = counts.get(c, 0) - nNine

    output = ""
    output += "0"*nZeros
    output += "1"*nOnes
    output += "2"*nTwos
    output += "3"*nThrees
    output += "4"*nFours
    output += "5"*nFives
    output += "6"*nSixs
    output += "7"*nSeven
    output += "8"*nEights
    output += "9"*nNine

    return output

T = int(raw_input())

for t in range(T):
    print "Case #{}: {}".format(t+1, solve())
