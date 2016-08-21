def read_integers(filename):
    with open(filename) as f:
        return map(int, f)

data = read_integers('data.txt')
cases = data[0]

checklist = [False, False, False, False, False, False, False, False, False, False]

for i in range(1, cases+1):
        for a in range(0,10):
            checklist[a] = False
	for j in range(1, 110):
		num = str(data[i]*j)
		for k in range(0, len(num)):
			for l in range(0,10):
				if num[k] == str(l):
					checklist[l] = True
                accept = True
		for k in range(0,10):
			if checklist[k] == False:
				accept = False
                                break
		if accept == True:
			break
        if accept == True:
            append = str(data[i]*j)
        else:
            append = 'INSOMNIA'
        print "Case #%d: %s" % (i, append)
