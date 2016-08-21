t = int(raw_input())  # read a line with a single integer

for i in xrange(1, t + 1):
    word =  raw_input()
    result = ''
    for j in word:
    	if result == '':
    		result+=j
    	elif j<result[0]:
    		result+=j
    	else:
    		result = j + result



    print "Case #{}: {}".format(i,result)
