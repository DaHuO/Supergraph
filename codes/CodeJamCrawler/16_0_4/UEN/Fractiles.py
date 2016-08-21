import sys

T = 0;
KCS = list();
with open("D-small-attempt1.in") as f :
	T = int(f.readline());
	for line in f :
		KCS.append([int(x) for x in line.split()]);

print type(T)
print KCS

with open("small-output.txt", 'w') as f :
	for i in range (0, T) :
		K = KCS[i][0];
		C = KCS[i][1];
		S = KCS[i][2];
		data = "Case #%d: " % (i+1);
		result = "";
		
		if K == 1 :
			result = "1\n";
		elif C == 1 :
			if K != S :
				result = "IMPOSSIBLE\n"
			else :
				for j in range(0, S-1) :
					result += "%d " % (j+1);
				result += "%d\n" % S;
		else :
			if (K-1) > S :
				result = "IMPOSSIBLE\n"
			else :
				for j in range(0, K-2) :
					result += "%d " % (2+j*(K+1));
				result += "%d\n" % (2+(K-2)*(K+1));

		f.write(data+result);

