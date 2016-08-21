filename = "C:\\Users\\Adarsh\\Documents\\Google codejam\\2016\\input.txt"
outputfilename= "C:\\Users\\Adarsh\\Documents\\Google codejam\\2016\\output.txt"
file = open(filename)
output = open(outputfilename, 'w')
T=int(file.readline())
for x in range(0,T):
	N=file.readline()
	digits=[0,0,0,0,0,0,0,0,0,0]
	if int(N) == 0:
		output.write("Case #"+str(x+1)+": INSOMNIA\n")
		continue
	else:
		count=0
		while digits!=[1,1,1,1,1,1,1,1,1,1]:
			count=count+1
			num=str(int(N)*(count))
			if count>10000000:
				print(count)
			for y in num:
				digits[int(y)]=1
		output.write("Case #"+str(x+1)+": "+num+"\n")