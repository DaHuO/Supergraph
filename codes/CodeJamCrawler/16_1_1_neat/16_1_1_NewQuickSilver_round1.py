n = int(input());
i = 0;
while(i<n):
	word = "";
	string = input();
	word += string[0];
	j = 1;
	while(j < len(string)):
		if(string[j]>word[0] or string[j] == word[0]):
			word = string[j]+word;
		if(string[j]<word[0]):
			word = word + string[j];
		j+=1;
	print("Case #"+str(i+1)+": "+word);
	i+=1;