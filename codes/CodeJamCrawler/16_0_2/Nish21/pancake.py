for t in range(int(input())):
	string = input()
	i, count, length = 0, 0, len(string)
	while(i<length):
		if(string[i]=='-'):
			while(i <length and string[i]=='-'):
				i+=1
			count += 1
		else:
			while(i < length and string[i]=='+'):
				i+=1
			if i < length:
				count+=1
	print("Case #"+str(t+1)+": "+str(count))
		
	
