import sys
i = 0
def get_happy_num(val):
	val = val.strip()
	val = val[::-1]
	count = 0
	for s in val:
		if s == '-':
			if count % 2 == 0:
				count = count + 1
		if s == '+':
			if count % 2 == 1:
				count = count + 1
	return count
for line in sys.stdin:
    val = line
    if i == 0:
    	i = 1
    	continue
    print "Case #"+str(i)+": "+str(get_happy_num(val))
    i = i + 1

