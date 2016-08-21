import numpy as np
import itertools
from collections import defaultdict
def check(board):
	
	for row in board:
		for i in xrange(len(row) - 1):
			if row[i] >= row[i+1]:
				return False

	for i in range(len(board)):

		for j in range(len(board) -1):
			if board[j][i] >= board[j+1][i]:
				return False

	# print '================'
	# print 'found board'
	# for l in board:
	# 	print l
	# print '================'

	return True

def solve(lines, n):
	
	for b in itertools.combinations(lines, n):
		# print b
		new_b = list(b)
		new_b.sort()
		
		if check(new_b):
			found_board = new_b
			cols = []
			for i in range(n):
				s = []
				for e in found_board:
					s.append(e[i])
				cols.append(s)

			col_count = 0
			no_col = None

			# for e in found_board:
				# print e
			
			content_dict = defaultdict(int)

			for e in found_board:
				# print 'row {0}'.format(e)
				content_dict[tuple(e)] += 1

			for e in cols:
				# print 'col {0}'.format(e)
				content_dict[tuple(e)] += 1

			for l in lines:
				# print 'l {0}'.format(l)
				content_dict[tuple(l)] -= 1

			minus_count = 0
			minus_ele = None
			# print content_dict
			for k in content_dict:
				if content_dict[k] > 0:
					# print k
					minus_count += 1
					minus_ele = k

			if minus_count != 1:
				continue


			for e in found_board:
				print e
			print content_dict
			print 'answer ' + ' '.join(map(str, minus_ele))
			return ' '.join(map(str, minus_ele))

	# if it gets here the board itself must be symmetrical
	for line in lines:
		if lines.count(line) != 2:
			print 'board symmetrical must be ' + ' '.join(map(str, line))
			return line

f_out = open('B_output.txt', 'w')
f_in = open('B-small-attempt3.in', 'r')

t = int(f_in.readline())
for idx in range(t):
	
	n = int(f_in.readline())

	lines = []
	for _ in range(2*n - 1):
		lines.append(f_in.readline())

	lines = [map(int, line.split()) for line in lines]
	print 'doing {0} case'.format(idx)

	lines.sort()
	print 'board'
	for line in lines:
		print line
	print '---------------------------'
	pos_ans = solve(lines, n)
	f_out.write("Case #{0}: {1}\n".format(idx+1, pos_ans))	

f_out.close()