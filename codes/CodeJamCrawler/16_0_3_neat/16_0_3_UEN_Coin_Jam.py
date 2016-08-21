def isPrime(x) :
	if x%2 == 0 :
		return 0;
	for i in range(3, int(x**0.5)+1):
		if x%i == 0:
			return 0;
	return 1;

def findDivisor(x) :
	for i in range(2, x) :
		if x%i == 0 :
			return i

import sys

NJ = [];
with open("C-large.in") as f :
	T = int(f.readline());
	for line in f :
		NJ = [int(x) for x in line.split()];

Count = 0;
Jam_coin = [1,0,0,0,0,0,0,1];
div_trick = [3,2,5,2,7,2,3,2,11];
Trick_Jam = list();
Trick_Jam32 = list();
#for i in range(0, 8) :
#	if i == 0 :
#		Jam_coin.append(1);
#	elif i == 7 :
#		Jam_coin.append(1);
#	else :
#		Jam_coin.append(0);


with open("output.txt", 'w') as f :
	data = "Case #%d:\n" % T;
	f.write(data);
	while True :
		isAllPrime = 0;
		div = [];
		Jam_number = [];
		data = "".join(str(c) for c in Jam_coin);
		#print Jam_coin;
		for i in range(2, 11) :
			tmp = long(data, i);
			Jam_number.append(tmp);
			if isPrime(tmp) == 1 :
				isAllPrime = 0;
				break;
			else :
				isAllPrime = 1;
		#print Jam_number;

		if isAllPrime == 1 :
			#Count += 1;
			#f.write(data);
			for k in range(0, 9) :
				if div_trick[k] != findDivisor(Jam_number[k]) :
					flag = 0;
					break;
				else :
					flag = 1;
			if flag == 1 :
				Trick_Jam.append(Jam_coin[:]);
				#f.write(data+" ");
				#f.write("3 2 5 2 7 2 3 2 11");
				#f.write("\n");
				#print (Jam_coin)
				
				#print(Trick_Jam)

		if Jam_coin.count(1) == 8 :
			break;

		for j in range(6, 0, -1) :
			if Jam_coin[j] == 0 :
				Jam_coin[j] = 1;
				break;
			else :
				Jam_coin[j] = 0;
	print (Trick_Jam);
	#print (NJ[0])
	
	#print (Trick_len)
	if NJ[0]%16 == 0 :
		count = 0;
		Trick_len = len(Trick_Jam);
		#print "iamin"
		for i in range(0, Trick_len) :
			data1 = "".join(str(c) for c in Trick_Jam[i]);
			for j in range(0, Trick_len) :
				data2 = "".join(str(c) for c in Trick_Jam[j]);
				if NJ[0] == 16 :
					f.write(data1+data2+" 3 2 5 2 7 2 3 2 11\n");
				elif NJ[0] == 32 :
					Trick_Jam32.append(Trick_Jam[i]+Trick_Jam[j]);
				print (data1+data2+" 3 2 5 2 7 2 3 2 11\n")
				count += 1;
				if count == NJ[1] :
					break;
			if count == NJ[1] :
				break;
		if NJ[0] == 32:
			count = 0;
			Trick_len = len(Trick_Jam32);
			#print "iamin"
			for i in range(0, Trick_len) :
				data1 = "".join(str(c) for c in Trick_Jam32[i]);
				for j in range(0, Trick_len) :
					data2 = "".join(str(c) for c in Trick_Jam32[j]);
					f.write(data1+data2+" 3 2 5 2 7 2 3 2 11\n");
					Trick_Jam32.append(Trick_Jam32[i]+Trick_Jam32[j]);
					print (data1+data2+" 3 2 5 2 7 2 3 2 11\n")
					count += 1;
					if count == NJ[1] :
						break;
				if count == NJ[1] :
					break;				

		




