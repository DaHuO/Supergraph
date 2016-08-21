# https://code.google.com/codejam/contest/6254486/dashboard#s=p1
import sys

class Pancakes(object):
    def __init__(self, vals):
        self.vals = list(vals)
        self.num_flips = 0

    def flip(self, i):
        self.vals[0:i+1] = reversed([(not val) for val in self.vals[0:i+1]])
        self.num_flips += 1
        #print 'flip', self.num_flips, self.vals, i

    def is_done(self):
        return all(self.vals)

def run(pancakes):
    # fix from the stop of the stack, making each pancake match the one below it
    for i in range(len(pancakes.vals)-1):
        if pancakes.vals[i] != pancakes.vals[i+1]:
            pancakes.flip(i)
    # last pancake's a special case since there's no next-pancake - maybe flip the whole stack
    last = len(pancakes.vals)-1
    if not pancakes.vals[last]:
        pancakes.flip(last)
    return pancakes.num_flips
    # NOPE. below solution solves it, with too many iterations!
    ## fix the bottom of the stack, working upward
    #for i in reversed(range(len(pancakes.vals))):
    #    #print 'pre', pancakes.vals
    #    if (not pancakes.vals[i]):
    #        # TODO optimize this by fixing multiple iterations at once!
    #        if (i != 0 and pancakes.vals[0]):
    #            pancakes.flip(0)
    #        pancakes.flip(i)
    #    assert pancakes.vals[i]
    #assert pancakes.is_done()
    #return pancakes.num_flips

def parse(lines):
    # true: happy-side-up, false: blank-side-up
    return Pancakes(char == '+' for char in lines.pop(0).strip())

def main(infile):
    lines = infile.readlines()
    count = int(lines.pop(0))
    cases = (parse(lines) for case in range(count))
    output = (run(case) for case in cases)
    for i, result in enumerate(output):
        print "Case #%d: %s" % (i + 1, result)

if __name__=='__main__':
    main(sys.stdin)
