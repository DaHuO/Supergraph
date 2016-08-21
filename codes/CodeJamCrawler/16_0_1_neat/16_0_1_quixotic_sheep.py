t = int(raw_input())
for i in xrange(1, t + 1):
  n = int(raw_input())
  if n == 0:
  	print "Case #{}: INSOMNIA".format(i)
  else:
  	num = range(0,10)
  	j = 1
  	answer = n
  	while len(num) != 0:
  		answer = j * n
  		nstr = str(answer)
  		for d in nstr:
  			if int(d) in num:
  				num.remove(int(d))
  		j += 1
  	print "Case #{}: {}".format(i, answer)