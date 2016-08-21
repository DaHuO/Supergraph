import sys

#T = int(input());
N = [];
Fall_asleep = {0,1,2,3,4,5,6,7,8,9};
with open("A-large.in") as f :
	T = int(f.readline());
	for line in f :
		N.append(long(line));
#for i in range(0, T) : 
#	N.append(long(input()));
with open("output.txt", 'w') as f :
	for i in range(0, T) :
		if N[i] == 0 : 
			print "Case #%d: INSOMNIA" % (i+1);
			data = "Case #%d: INSOMNIA\n" % (i+1);
			f.write(data);
		else :
			Named = set();
			For_check_digits = str(N[i]);
			Last_N = long(N[i]);
			while True :
				for c in For_check_digits :
					Named.add(int(c));
				#print(Named)
				if len(Fall_asleep - Named) == 0 :
					break;
				else :
					Last_N += N[i];
					For_check_digits = str(Last_N);
			print "Case #%d: %d" % (i+1, Last_N);
			data = "Case #%d: %d\n" % (i+1, Last_N);
			f.write(data);
