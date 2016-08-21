from optparse import OptionParser

def fall_asleep_number(nb):
    digits_seen = set()
    if nb == 0:
        return "INSOMNIA"
    digits_seen |= set(list(str(nb)))
    sumnb = nb
    while len(digits_seen) != 10:
        sumnb += nb 
        digits_seen |= set(list(str(sumnb)))
    return sumnb
    
def problem_A(filename):
    with open(filename, 'rU') as fin:
        lines = [l.rstrip("\n") for l in fin.readlines()]
    ntestcases = int(lines[0])
    for i in range(ntestcases):
        print "Case #%d: %s" % (i+1, fall_asleep_number(int(lines[i+1])))





if __name__ == "__main__":
    problem_A("A-large.in")
