import sys
import os
import glob

input_file = None
def readone(t): return t(input_file.readline().strip())
def readmany(t): return map(t, input_file.readline().split())

def remlet(s, w, c):
    for letter in w:
        s = s.replace(letter, '', c)
    return s

def solve():
    s = readone(str)
    '''
    
    Z O
    ON
    W O
    HR
    U FO
    FV I
    X I
    VN
    HI
    NN
    '''
    s = str(sorted(s))
    count = [0] * 10
    count[6] = s.count('X')
    s = remlet(s, 'SIX', count[6])
    count[4] = s.count('U')
    s = remlet(s, 'FOUR', count[4])
    count[0] = s.count('Z')
    s = remlet(s, 'ZERO', count[0])
    count[3] = s.count('R')
    s = remlet(s, 'THREE', count[3])
    count[8] = s.count('H')
    s = remlet(s, 'EIGHT', count[8])
    count[2] = s.count('W')
    s = remlet(s, 'TWO', count[2])
    count[5] = s.count('F')
    s = remlet(s, 'FIVE', count[5])
    count[7] = s.count('V')
    s = remlet(s, 'SEVEN', count[7])
    count[1] = s.count('O')
    s = remlet(s, 'ONE', count[1])
    count[9] = s.count('I')
    s = remlet(s, 'NINE', count[9])
    retval = []
    for r in range(10):
        retval.extend([str(r)] * count[r])
    return ''.join(retval)

if __name__ == '__main__':
    input_file = sys.stdin
    problem = os.path.split(__file__)[1][0].upper()
    output_filename = 'test.out'
    inputs = glob.glob(os.path.expanduser('~') + '/Downloads/' + problem + '-*.in')
    newest = max(inputs, key=os.path.getctime)
    input_filename = os.path.split(newest)[1]
    output_filename = problem + '-' + input_filename.split('-')[1][:-3] + '.out'
    input_file = open(newest)
    T = int(input_file.readline().strip())
    output_file = open(output_filename, 'w')
    for t in xrange(T):
        result = solve()
        output_file.write("Case #%d: %s\n" % (t + 1, result))
        print "Case #%d: %s" % (t + 1, result)
    