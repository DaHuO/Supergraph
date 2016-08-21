
numbers=[int(line.rstrip('\n')) for line in open('Downloads/A-large.in')]
del numbers[0]
print numbers
count=1
for n in numbers:

	if n==0:
		print 'Case #'+str(count)+': INSOMNIA'
	else:	
		i=1
		digitdict={
				'1':False,
				'2':False,
				'3':False,
				'4':False,
				'5':False,
				'6':False,
				'7':False,
				'8':False,
				'9':False,
				'0':False,
				}
		while True:
		
			temp=n*i
			x=temp
			#print 'temp='+str(temp)
			while temp!=0:
				digit=temp%10
				temp=temp/10
				digitdict[str(digit)]=True
				#print 'digitdict['+str(digit)+']='+str(digitdict['1'])
			if digitdict['0'] is True and digitdict['1'] is True and digitdict['2'] is True and digitdict['3'] is True and digitdict['4'] is True and digitdict['5'] is True and digitdict['6'] is True and digitdict['7'] is True and digitdict['8'] is True and digitdict['9'] is True:
				print 'Case #'+str(count)+': ' + str(x)
				break
			i=i+1
	count+=1

