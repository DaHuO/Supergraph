#exec(open('C:/Users/Taili/Desktop/google-code-jam/round-one-2/r2.py').read())
def r3_run(stack):
	stk =stack
	count = 0
	while(stk.find('-') != -1):
		if(stk[0] == '-' and stk.find('+') != -1):
			stk = stk.find('+')*'+' + stk[stk.find('+'):]
			count += 1
		elif(stk[0] == '+'):
			stk = stk.find('-')*'-' + stk[stk.find('-'):]
			count += 1
		else:
			return count+1
	return count

foldername = "round-one-2"
filename = "B-large"
f = open('C:/Users/Taili/Desktop/google-code-jam/%s/%s.in' %(foldername,filename), 'r')
outputfile = open('C:/Users/Taili/Desktop/google-code-jam/%s/%s.out' %(foldername,filename), 'w')
count = 0
for line in f:
	if count == 0: 
		count += 1 
		continue
	line = line.split('\n')

	#logic part
	print "Case #%d: %d" % (count , r3_run(line[0]))
	s = "Case #%d: %d" % (count , r3_run(line[0]))
	outputfile.write(s+'\n')
	count += 1
f.close()
outputfile.close()	

	



