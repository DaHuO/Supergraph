def solve(s):
    soln = []
    while "G" in s:
        removeLetters(s, "EIGHT")
        soln.append(8)
    while "Z" in s:
        removeLetters(s, "ZERO")
        soln.append(0)
    while "W" in s:
        removeLetters(s, "TWO")
        soln.append(2)
    while "U" in s:
        removeLetters(s, "FOUR")
        soln.append(4)
    while "O" in s:
        removeLetters(s, "ONE")
        soln.append(1)
    # THREE, FIVE, SIX, SEVEN, NINE
    while "X" in s:
        removeLetters(s, "SIX")
        soln.append(6)
    # THREE, FIVE, SEVEN, NINE
    while "R" in s:
        removeLetters(s, "THREE")
        soln.append(3)
    # FIVE, SEVEN, NINE
    while "F" in s:
        removeLetters(s, "FIVE")
        soln.append(5)
    while "S" in s:
        removeLetters(s, "SEVEN")
        soln.append(7)
    while "N" in s:
        removeLetters(s, "NINE")
        soln.append(9)

    return "".join(sorted([str(n) for n in soln]))

def removeLetters(s, word):
    for c in word:
        s.remove(c)

fin = open("A-large.in", "r")
fout = open("A-large.out", "w")

for t in xrange(1, int(fin.readline()) + 1):
    sln = solve(list(fin.readline()))
    fout.write("Case #" + str(t) + ": " + str(sln) + "\n")

fout.close()
