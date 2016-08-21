import sys

for line in sys.stdin:
    for var in line.split():
    	var = int(var)
# a = raw_input()
# b = raw_input()
# c = raw_input() 

print "Case #1:"

for i in xrange(0, 500):
	st = '1' + format(i,'014b') + '1'
	print st+st,
	for j in xrange(2,11):
		print (j**16 + 1),
	print ""
