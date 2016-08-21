f = open('A-large.in')
count = int(f.readline())
for i in range(1,count+1):
	number = int(f.readline())
	#print ('number is '+ str(number))
	answer = 0
	dict = {}
	keep_running = True
	n = 1
	while keep_running:
		if number == 0:
			answer = 'INSOMNIA'
			keep_running = False
			break
		fnumber = number*n
		num_string = str(fnumber)
		for ch in num_string:
			#print ('string in '+ num_string + ' is ' + ch)
			dict[ch] = True
		if len(dict) == 10:
			answer = fnumber
			keep_running = False
			break
		n=n+1
	print ('CASE #'+str(i)+': '+str(answer))

			
f.close()


