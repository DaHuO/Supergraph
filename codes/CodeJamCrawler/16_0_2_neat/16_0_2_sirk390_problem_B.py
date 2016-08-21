import itertools

def nbmin_flips(pancakes):
    uniq = [k for k, _v in itertools.groupby(list(pancakes))]
    if uniq[-1] == "+":
        uniq.pop()
    return len(uniq)  
    
    
def problem_B(filename):
    with open(filename, 'rU') as fin:
        lines = [l.rstrip("\n") for l in fin.readlines()]
    ntestcases = int(lines[0])
    for i in range(ntestcases):
        print "Case #%d: %s" % (i+1, nbmin_flips(lines[i+1]))


if __name__ == "__main__":
    problem_B("B-large.in")
