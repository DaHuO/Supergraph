import sys

inf = sys.argv[1]

f = open(inf, 'rU')
outf = open(inf + ".out", 'w')


def get_hist(s):
    hist = {}
    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        hist[i] = 0
    for c in s:
        o = hist.get(c, 0)
        hist[c] = o + 1
    return hist

def sub_hist(a, b, times):
    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        a[i] -= b[i] * times

digits = {
    0: "ZERO",
    1: "ONE",
    2: "TWO",
    3: "THREE",
    4: "FOUR",
    5: "FIVE",
    6: "SIX",
    7: "SEVEN",
    8: "EIGHT",
    9: "NINE"
}


digit_occurrences = [0] * 10
for i in xrange(0, 10):
    digit_occurrences[i] = get_hist(digits[i])

T = int(f.readline())
for t in xrange(T):

    s = f.readline().strip()


    counts = [0] * 10

    occurrences = get_hist(s)

    counts[0] = occurrences['Z']
    sub_hist(occurrences, digit_occurrences[0], counts[0])
    counts[6] = occurrences['X']
    sub_hist(occurrences, digit_occurrences[6], counts[6])
    counts[7] = occurrences['S']
    sub_hist(occurrences, digit_occurrences[7], counts[7])
    counts[5] = occurrences['V']
    sub_hist(occurrences, digit_occurrences[5], counts[5])
    counts[4] = occurrences['F']
    sub_hist(occurrences, digit_occurrences[4], counts[4])
    counts[3] = occurrences['R']
    sub_hist(occurrences, digit_occurrences[3], counts[3])
    counts[2] = occurrences['W']
    sub_hist(occurrences, digit_occurrences[2], counts[2])
    counts[8] = occurrences['T']
    sub_hist(occurrences, digit_occurrences[8], counts[8])
    counts[1] = occurrences['O']
    sub_hist(occurrences, digit_occurrences[1], counts[1])
    counts[9] = occurrences['I']
    sub_hist(occurrences, digit_occurrences[9], counts[9])

    out = ""
    for i in xrange(0, 10):
        out += str(i) * counts[i]

    for key in occurrences:
        if occurrences[key] != 0:
            print key, "HELP"
    print out
    outf.write("Case #{0}: {1}\n".format(t+1, out))

f.close()
outf.close()
