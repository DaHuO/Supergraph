tc = int(raw_input())
for cn in range(tc):
	x = int(raw_input())
	n = set()
	j = 1
	while j>0:
		val = j*x
		j = j+1
		if x==0:
			print "Case #"+str(cn+1)+": INSOMNIA"
			break
		n.update([int(i) for i in str(val)])
		if n == set([i for i in range(10)]):
			print "Case #"+str(cn+1)+":",val
			break