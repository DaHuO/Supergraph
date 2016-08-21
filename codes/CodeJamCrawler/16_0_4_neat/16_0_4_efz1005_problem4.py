__author__ = "Enric Florit <efz1005@gmail.com>"

num_test_cases = int(raw_input())
cases = []
for i in xrange(num_test_cases):
	cases.append([int(i) for i in raw_input().split(" ")])

for i in xrange(num_test_cases):
	print "Case #" + str(i + 1) + ":",
	for j in xrange(1, cases[i][0] + 1):
		print str(j),
	print