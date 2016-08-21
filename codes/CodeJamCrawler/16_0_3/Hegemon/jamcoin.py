filename = "C:\\Users\\Adarsh\\Documents\\Google codejam\\2016\\input.txt"
outputfilename= "C:\\Users\\Adarsh\\Documents\\Google codejam\\2016\\output.txt"
file = open(filename)
output = open(outputfilename, 'w')
T=int(file.readline())
for x in range(0,T):
	line=file.readline().strip('\t\n\r').split(' ')
	N=int(line[0])
	J=int(line[1])
	generated=0
	output.write("Case #"+str(x+1)+":\n")
	if N==32:
		num=[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
		max=1073741824
	if N==16:
		num=[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
		max=16384
	else:
		num=[1,0,0,0,0,1]
		max=16
	count=0
	for y in range(max):
		num="1"+str(bin(y)[2:].zfill(N-2))+"1"
		divisors=[0,0,0,0,0,0,0,0,0]
		success=1
		for base in range(2,11):
			basenum=int(num,base)
			i=2
			notprime=0
			while i*i<=basenum:
				if basenum%i==0:
					divisors[base-2]=i
					notprime=1
					break
				if i==2 :
					i=i+1
				else:
					i=i+2
			if notprime==0:
				success=0
				break
		if (success==0):
			continue
		else:
			output.write(num)
			for divs in divisors:
				output.write(" "+str(divs))
			output.write("\n")
			count=count+1
			print("count= "+str(count))
			if count==J:
				exit()