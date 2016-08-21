from sets import Set
t = input()
t1 = t
final = ""
while t:
	n = input()
	if n == 0:
		answer = "INSOMNIA"
	else:
		cond = True
		digits = Set()
		number = n
		c = 1
		while(cond):
			for i in str(n):
				digits.add(i)
			if len(digits)==10:
				answer = n
				cond = False;
			else:
				c+=1
				n=number*c
	final+="Case #{0}: {1}\n".format(t1-t+1, answer)
	#print "Case #"+t1-t+1,":",answer 
	t-=1
print final
output_file = open('q1_large.out','w')
output_file.write("{}".format(final))
output_file.close()
	
def findAllDigits(n):
	return [i for i in str(n)]