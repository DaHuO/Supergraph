import sys

T = int(input())

words = [
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

def rem_num(m, num, n):
    for c in num:
        m[c] = m[c] - n

for t in range(T):

    S = str(input())

    m = {}
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for c in letters:
        m[c] = 0

    counts = [0] * 10

    for c in S:
        if c in m:
            m[c] += 1
        else:
            m[c] = 1

    counts[0] = m["Z"]
    rem_num(m, words[0], counts[0])
    counts[2] = m["W"]
    rem_num(m, words[2], counts[2])
    counts[6] = m["X"]
    rem_num(m, words[6], counts[6])
    counts[7] = m["S"]
    rem_num(m, words[7], counts[7])
    counts[8] = m["G"]
    rem_num(m, words[8], counts[8])
    counts[3] = m["H"]
    rem_num(m, words[3], counts[3])
    counts[5] = m["V"]
    rem_num(m, words[5], counts[5])
    counts[4] = m["F"]
    rem_num(m, words[4], counts[4])
    counts[9] = m["I"]
    rem_num(m, words[9], counts[9])
    counts[1] = m["O"]
    rem_num(m, words[1], counts[1])

    sys.stdout.write("Case #" + str(t+1) + ": ")
    for i, n in enumerate(counts):
        if n != 0:
            for j in range(n):
                sys.stdout.write(str(i))
    sys.stdout.write("\n")
