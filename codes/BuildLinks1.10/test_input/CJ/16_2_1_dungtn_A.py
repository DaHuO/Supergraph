import sys, pdb


digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

distinct_even_chrs = {
    "Z": 0,
    "W": 2,
    "U": 4,
    "X": 6,
    "G": 8
}

distinct_odd_chrs = {
    "O": 1,
    "T": 3,
    "F": 5,
    "S": 7,
}


def to_digits(text):
    ans = []
    for chr, val in distinct_even_chrs.iteritems():
        while chr in text:
            ans.append(val)
            for c in digits[val]:
                text.remove(c)
    if len(text) > 0:
        for chr, val in distinct_odd_chrs.iteritems():
            while chr in text:
                ans.append(val)
                for c in digits[val]:
                    text.remove(c)
    if len(text) > 0:
        chr, val = "N", 9
        while chr in text:
            ans.append(val)
            for c in digits[val]:
                text.remove(c)
    return "".join([str(x) for x in sorted(ans)])


def main():
    f = open(sys.argv[1], 'r')
    T = int(f.readline().strip())

    for t in xrange(T):
        text = f.readline().strip()
        print "Case #{0}: {1}".format(t+1, to_digits(list(text)))


if __name__=="__main__":
    main()