f = open('sheep2.in','r')
f2 = open('result.txt','w')
a = f.readlines()
print a
for i in xrange(0,len(a)):
	a[i]=int(a[i].strip())

for i in xrange(1,len(a)):
	print a[i]
	if a[i]==0:
		f2.write('Case #'+str(i)+': INSOMNIA\n')
		continue			
	digit_dictionary={}
	for j in xrange(0,10):
		digit_dictionary[j]=0
	flag = 0	
	temp_number=a[i]
	while flag == 0:	
		number = temp_number
		#print number
		while number!=0:
			digit_dictionary[number%10]=1
			number = number/10
		sleep = 1
		for k in digit_dictionary:
			if digit_dictionary[k]!=1:
				sleep=0
		if sleep==0:		
			temp_number+=a[i]
			#print temp_number,a[i]
			#print "HERE"
		else:
			f2.write('Case #'+str(i)+': '+str(temp_number)+'\n')
			print "Done"
			flag=1

