from collections import Counter

NAMES = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def digits(strvalue):
    counts = Counter(strvalue)
    zeros = counts["Z"]
    twos = counts["W"]
    fours = counts["U"]
    sixs = counts["X"]
    sevens = counts["S"] - sixs
    fives = counts["V"] - sevens
    eights = counts["G"]
    nines = counts["I"] - eights - sixs - fives
    threes = counts["H"] - eights
    ones = counts["O"] - fours - zeros - twos 
    digits_counts = [zeros, ones, twos, threes, fours, fives, sixs, sevens, eights, nines]
    result = "".join([name * count for name, count in zip(NAMES, digits_counts)])
    assert len(result) == len(strvalue)
    assert sorted(result) == sorted(strvalue)  
    return  "".join([str(digit) * count for digit, count in zip(range(10), digits_counts)])
    
def problem_A(filename):
    with open(filename, 'rU') as fin:
        lines = [l.rstrip("\n") for l in fin.readlines()]
    ntestcases = int(lines[0])
    for i in range(ntestcases):
        print "Case #%d: %s" % (i+1, digits(lines[i+1]))





if __name__ == "__main__":
    problem_A("A-large.in")
