from collections import defaultdict

def main(letter_dict):
    #print "START DICT!", letter_dict
    digits = parse_uniques(letter_dict)
    digits.sort()
    return ''.join([str(i) for i in digits])

#extract knowable digits out and reduce letter counts
def parse_uniques(d):
    digits = []
    if d['Z'] > 0:
        ##print "ZERO! this many times:", d['Z']
        digits += [0] * d['Z']
        decrement(d, 'E', d['Z'])
        decrement(d, 'R', d['Z'])
        decrement(d, 'O', d['Z'])
        decrement(d, 'Z', d['Z'])
    if d['W'] > 0:
        #print "TWO! this many times:", d['W']
        digits += [2] * d['W']
        decrement(d, 'T', d['W'])
        decrement(d, 'O', d['W'])
        decrement(d, 'W', d['W'])
    if d['U'] > 0:
        digits += [4] * d['U']
        decrement(d, 'F', d['U'])
        decrement(d, 'O', d['U'])
        decrement(d, 'R', d['U'])
        decrement(d, 'U', d['U'])
    if d['X'] > 0:
        digits += [6] * d['X']
        decrement(d, 'S', d['X'])
        decrement(d, 'I', d['X'])
        decrement(d, 'X', d['X'])
    if d['G'] > 0:
        digits += [8] * d['G']
        decrement(d, 'E', d['G'])
        decrement(d, 'I', d['G'])
        decrement(d, 'H', d['G'])
        decrement(d, 'T', d['G'])
        decrement(d, 'G', d['G'])
    #Now we can do some more
    #ONE THREE FIVE SEVEN NINE
    if d['O'] > 0: #now one
        #print "ONE! this many times:", d['O']
        digits += [1] * d['O']
        decrement(d, 'E', d['O'])
        decrement(d, 'N', d['O'])
        decrement(d, 'O', d['O'])
    if d['S'] > 0:
        digits += [7] * d['S']
        decrement(d, 'E', d['S'])
        decrement(d, 'V', d['S'])
        decrement(d, 'E', d['S'])
        decrement(d, 'N', d['S'])
        decrement(d, 'S', d['S'])
    if d['F'] > 0:
        digits += [5] * d['F']
        decrement(d, 'I', d['F'])
        decrement(d, 'V', d['F'])
        decrement(d, 'E', d['F'])
        decrement(d, 'F', d['F'])
    #Just leaves THREE NINE
    #print d
    digits += [3] * d['T']
    assert d['T'] == d['R']
    digits += [9] * d['I']
    assert d['N'] == 2 * d['I']
    return digits

def decrement(d, letter, count):
    d[letter] = d[letter] - count
    assert d[letter] > -1

    
if __name__=="__main__":
    t = int(raw_input())  # read a line with a single integer
    for test in xrange(1, t + 1):
	#PER TEST CASE HERE
	d = defaultdict(int)
	for letter in list(raw_input()):# read a list of integers, 2 in this case
	    d[letter] += 1
        print "Case #{}: {}".format(test, main(d))
# check out .format's specification for more formatting options
