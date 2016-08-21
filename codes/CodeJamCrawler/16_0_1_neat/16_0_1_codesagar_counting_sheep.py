inpt = open('input','r')
oupt = open('output','w')

n = inpt.readline().rstrip('\n')
#n = raw_input('')
for z in range(int(n)):
	x = inpt.readline().rstrip('\n')
#	x = raw_input('')
	if(x != '0'):
		num = int(x)
		cnt = 1
		status = [0] * 10
		true = [1] * 10
		gate = 1
		while(gate):
			for i in str(num):
				status[int(i)]=1
			num = int(x) * cnt
			cnt = cnt+1
			if(status == true):
				cnt = cnt-2
				gate = 0
		ou = 'Case #'+str(z+1)+': '+str(int(x)*cnt)+'\n'
		oupt.write(ou)
	else:
		ou = 'Case #'+str(z+1)+': '+'INSOMNIA'+'\n'
		oupt.write(ou)



