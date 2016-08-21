
with open("A-large.in") as f:
    content = f.readlines()
    
for i in range(len(content)):
    content[i]=int(content[i])
text_file = open("output.txt", "w")
x=content[0]
t=1
while t<=x:
	array=[]

	number=content[t]
	num=number
	j=1
	while True:
		if number==0:
			output='INSOMNIA'
			break
		string=str(number)
		for i in range(len(string)):
			if string[i] not in array:
				array.append(string[i])
		j+=1
		
		if len(array)==10:
			output=number
			break
		number=j*num
	text_file.write("Case #%s: %s\n" % (str(t), str(output)))

	t+=1
text_file.close()