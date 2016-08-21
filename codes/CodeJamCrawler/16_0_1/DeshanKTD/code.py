f = open('output.txt','w')
test = int(input())


for i in range(test):
	a = set()
	number = int(input())
	
	if number == 0:
		print('INSOMNIA')
		f.write('Case #'+str(i+1)+': INSOMNIA\n')
	
	else:
		j = 1;
		while len(a)!=10:
			change = number * j
			change = str(change)
			for k in range(len(change)):
				if change[k].isdigit():
					a.add(change[k])
			#print(str(len(a))+ str(a)+ str(change))
			j=j+1
			
		print(change)
		f.write('Case #'+str(i+1)+': '+ change+'\n')
		
			
				
	
	
	