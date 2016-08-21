import sys
import os
import glob

input_file = None
def readone(t): return t(input_file.readline().strip())
def readmany(t): return map(t, input_file.readline().split())

def solve():
	word = readone(str)
	letters = [word[0]]
	for letter in word[1:]:
		if letter >= letters[0]:
			letters = [letter] + letters
		else:
			letters.append(letter)
	return ''.join(letters)

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
	