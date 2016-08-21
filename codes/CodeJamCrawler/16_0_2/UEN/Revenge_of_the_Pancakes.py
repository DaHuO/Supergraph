import sys

N = [];
with open("B-large.in") as f :
	T = int(f.readline());
	for line in f :
		N.append(line);

with open("output.txt", 'w') as f :
	for i in range(0, T) :
		Pancake_status = list(N[i]);
		if '\n' in Pancake_status : 
			Pancake_status.remove('\n');
		Pancake_Number = len(Pancake_status);
		#print (Pancake_status)
		#print (Pancake_Number)
		Maneuver_count = 0;
		for j in range(0, Pancake_Number) :
			if Pancake_status[Pancake_Number-j-1] == '+' :
				pass;
			else :
				Pancake_status[Pancake_Number-j-1] = '+';
				for k in range(0, Pancake_Number-j-1) :
					if Pancake_status[k] == '-' :
						Pancake_status[k] = '+';
					else :
						Pancake_status[k] = '-';
				#print (Pancake_status)
				Maneuver_count += 1;
		print "Case #%d: %d" % (i+1, Maneuver_count);
		data = "Case #%d: %d\n" % (i+1, Maneuver_count);
		f.write(data);
