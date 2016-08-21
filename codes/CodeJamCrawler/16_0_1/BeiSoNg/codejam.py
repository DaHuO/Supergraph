def calculate( originalstr ):
	for digit in originalstr:
		singledigit = int(digit)
		if singledigit in allnumbers:
			#print 'Digits found', singledigit
			allnumbers.remove(singledigit);

	if not allnumbers:
		return True
	else:
		return False

def checkempty (bool):
	if bool:
		print "LIST IS EMPTY"
	else:
		print" LIST IS NOT EMPTY"
   
   
f = open('A-large.in', 'r')
o = open('A-small-practice.out', 'w')

T = int(f.readline().strip())

for t in xrange(T):

	originalstr = f.readline().strip()
	
	allnumbers=[0,1,2,3,4,5,6,7,8,9]

	for x in range(1, 250):
		multiplenow = str(int(originalstr)*x)
		bool = calculate(multiplenow)
		# checkempty(bool)
		#print multiplenow
		if(bool):
			s = "Case #%d: %s\n" % (t+1, multiplenow)
			print s
			o.write(s)

			break
		if x==249:
			s = "Case #%d: %s\n" % (t+1, "INSOMNIA")
			print s	
			o.write(s)


	# s = "Case #%d: %s\n" % (t+1, originalstr)
	# print s
print "This line will be printed."

