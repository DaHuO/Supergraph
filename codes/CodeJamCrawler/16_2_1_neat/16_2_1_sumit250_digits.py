t = int(input())
for i in range(t):
	stri = input()
	freq = dict()
	for letter in stri:
		if(letter in freq):
			freq[letter]+=1
		else:
			freq[letter]=1
	
	ans = ''
	if('Z' in freq and freq['Z']!=0):
		num = freq['Z']
		freq['Z']-=num
		freq['E']-=num
		freq['R']-=num
		freq['O']-=num
		ans+= '0'*num
	if('W' in freq and freq['W']!=0):
		num = freq['W']
		freq['T']-=num
		freq['W']-=num
		freq['O']-=num
		ans+= '2'*num
	if('U' in freq and freq['U']!=0):
		num = freq['U']
		freq['F']-=num
		freq['U']-=num
		freq['O']-=num
		freq['R']-=num
		ans+= '4'*num
	if('X' in freq and freq['X']!=0):
		num = freq['X']
		freq['S']-=num
		freq['I']-=num
		freq['X']-=num
		ans+= '6'*num
	if('G' in freq and freq['G']!=0):
		num = freq['G']
		freq['E']-=num
		freq['I']-=num
		freq['G']-=num
		freq['H']-=num
		freq['T']-=num
		ans+= '8'*num
	if('S' in freq and freq['S']!=0):
		num = freq['S']
		freq['S']-=num
		freq['E']-=num
		freq['V']-=num
		freq['E']-=num
		freq['N']-=num
		ans+= '7'*num
	if('T' in freq and freq['T']!=0):
		num = freq['T']
		freq['T']-=num
		freq['H']-=num
		freq['R']-=num
		freq['E']-=num
		freq['E']-=num
		ans+= '3'*num
	if('V' in freq and freq['V']!=0):
		num = freq['V']
		freq['F']-=num
		freq['I']-=num
		freq['V']-=num
		freq['E']-=num
		ans+= '5'*num
	if('O' in freq and freq['O']!=0):
		num = freq['O']
		freq['O']-=num
		freq['N']-=num
		freq['E']-=num
		ans+= '1'*num
	if('I' in freq and freq['I']!=0):
		num = freq['I']
		freq['N']-=num
		freq['I']-=num
		freq['N']-=num
		freq['E']-=num
		ans+= '9'*num
	ans2 = sorted(ans)
	ans2 = "".join(ans2)
	j=i+1
	print("Case #"+str(j)+":",end=" ")
	print(ans2)
	
		

