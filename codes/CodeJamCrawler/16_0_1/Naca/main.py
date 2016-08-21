T = int(input());
data = [];
for i in range(T) :
	data.append(int(input()));

for i in range(T) :
	if (data[i] == 0) :
		print("Case #" + str(i + 1) + ": INSOMNIA");
	else :
		digits = [];
		sumN = data[i];
		while (len(digits) < 10) :
			tmp = sumN;
			while (tmp > 0) :
				if (tmp % 10 not in digits) :
					digits.append(tmp % 10);
				tmp //= 10;
			sumN += data[i];
		print("Case #" + str(i + 1) + ": " + str(sumN - data[i]));