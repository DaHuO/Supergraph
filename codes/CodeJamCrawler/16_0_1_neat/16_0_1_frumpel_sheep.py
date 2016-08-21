"""
Author: Rudolf Potucek
Use: CodeJam 2016 qualification 1 - brute force
"""

def read_data(filename):
	try:
		fh = open(filename,'r')
	except:
		print "ERROR: file not found"
		return []

	# Wrapping the whole read here is fine because I need a consistent read
	try:
		data = []
		lines = int(fh.readline())
		for ii in range(lines):
			data += [int(fh.readline())]
		return data
	except:
		print "ERROR: file format issues"
		return []

def blearix_count(start):
	seen = [0 for x in range(10)]
	last = None
	for ii in range(1,1000):
		check = start * ii
		if check == last:
			return "INSOMNIA"
		for jj in str(check):
			# print "dbg",ii,check,jj
			seen[int(jj)] = 1
		if sum(seen) >= 10:
			return check
		last = check
	return "INSOMNIA-ISH"



count = 0
# for ii in range(1000001):
for ii in read_data('A-large.in'):
	count += 1
	print "Case #%d: %s" % (count,str(blearix_count(ii)))

