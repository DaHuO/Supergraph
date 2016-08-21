#f1 = open("A-small-attempt0.in","r")
#f2= open("A-small-attempt0.out","w+")
f1 = open("A-large.in","r")
f2= open("A-large.out","w")
t = int(f1.readline())
for i in xrange(t):
	digit_map = {}
	n = int(f1.readline())
	#print digit_map
	if n == 0:
		f2.write("Case #"+str(i+1)+": INSOMNIA\n")
	else:
		count = 1
		number = n
		while len(digit_map) != 10:
			for digits in str(number):
				digit_map[digits] = 1
			count += 1
			number = n * count
			#print digit_map, number
		print n* (count-1)
		f2.write("Case #"+str(i+1)+": "+str(n*(count-1))+"\n")

	#print s_list
	#s_list.reverse()
	#f2.write("Case #"+str(i+1)+": "+' '.join(s_list)+"\n")
f1.close()	
f2.close()