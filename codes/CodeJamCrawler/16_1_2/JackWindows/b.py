#!/usr/bin/python

import sys

if len(sys.argv) != 2:
	print "usage: ./b.py <input_file_name>"
	exit()

input_file_name = sys.argv[1]
if input_file_name[-3:] == ".in":
	output_file_name = input_file_name[:-3] + ".out"
else:
	output_file_name = input_file_name + ".out"

def if_valid_successor(rc, b, cr):
	a = []
	for i in xrange(len(rc)):
		a = rc[len(rc) - 1 - i]
		if a:
			break
	if a:
		for i in xrange(len(a)):
			if not a[i] < b[i]:
				return False
	l = len(cr)
	for i in xrange(l):
		if cr[i] and b[i] != cr[i][l]:
			return False
	return True

def dfs(n):
	if n >= N:
		global Row, Column
		Row = row[:]
		Column = column[:]
		return
	canadiate = sorted_data[n]
	if n == 0:
		row.append(canadiate[0])
		if len(canadiate) > 1:
			column.append(canadiate[1])
		else:
			column.append([])
		dfs(n + 1)
		row.pop()
		column.pop()
	else:
		if len(canadiate) == 1:
			if if_valid_successor(row, canadiate[0], column):
				row.append(canadiate[0])
				column.append([])
				dfs(n + 1)
				row.pop()
				column.pop()
			if if_valid_successor(column, canadiate[0], row):
				column.append(canadiate[0])
				row.append([])
				dfs(n + 1)
				column.pop()
				row.pop()
		else:
			if if_valid_successor(row, canadiate[0], column) and if_valid_successor(column, canadiate[1], row):
				row.append(canadiate[0])
				column.append(canadiate[1])
				dfs(n + 1)
				row.pop()
				column.pop()
			if if_valid_successor(row, canadiate[1], column) and if_valid_successor(column, canadiate[0], row):
				column.append(canadiate[0])
				row.append(canadiate[1])
				dfs(n + 1)
				column.pop()
				row.pop()
	return

results = []
Row = []
Column = []
row = []
column = []
sorted_data = []
N = 0
with open(input_file_name, 'r') as f:
	T = int(f.readline())
	for t in xrange(T):
		N = int(f.readline())
		data = []
		for n in xrange(2 * N - 1):
			s = f.readline()
			s = s[:-1]
			d = [int(h) for h in s.split(' ')]
			data.append(d)
		missing_index = 0
		row = []
		column = []
		sorted_data = []
		for i in range(N):
			data.sort(key=lambda x:x [i], reverse=True)
			if len(data) == 1:
				missing_index = i
				sorted_data.append([data.pop()])
			else:
				if data[-1][i] == data[-2][i]:
					tmp = []
					tmp.append(data.pop())
					tmp.append(data.pop())
					sorted_data.append(tmp)
				else:
					missing_index = i
					sorted_data.append([data.pop()])
		dfs(0)
		#print Row
		#print Column
		ret = ''
		if Row[missing_index]:
			for i in xrange(N):
				ret += str(Row[i][missing_index]) + ' '
		else:
			for i in xrange(N):
				ret += str(Column[i][missing_index]) + ' '
		ret = ret[:-1]
		#print ret
		results.append(ret)

with open(output_file_name, 'w') as f:
	for i in range(len(results)):
		output_string = "Case #%d: %s\n" % (i + 1, results[i])
		print output_string[:-1]
		f.write(output_string)
