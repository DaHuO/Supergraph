import sys

N = list()
with open("A-large.in") as f :
	T = int(f.readline());
	for line in f :
		N.append(line);

with open("A-large.txt", 'w') as f :
	for i in range(0, T) :
		f.write("Case #%d: "% (i+1)) 
		str_list = list(N[i]);
		if '\t' in str_list :
			str_list.remove('\t');
		elif '\n' in str_list :
			str_list.remove('\n');
		#print(str_list)
		answer = list();
		for j in range(0,len(str_list)) :
			if len(answer) == 0 :
				answer.append(str_list[j]);
			else :
				if str_list[j] >= answer[0] :
					answer.append(str_list[j]);
					answer[1:j+1] = answer[0:j];
					answer[0] = str_list[j];
				else :
					answer.append(str_list[j]);
			#print(answer)
			
		data = "".join(answer);
		f.write(data+"\n");
