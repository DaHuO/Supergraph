T = int(input());
data = [];
for i in range(T) :
	data.append(input());

for i in range(T) :
	count = 0;

	if (len(data[i]) > 1) :
		lastSign = data[i][0];

		for k in range(1, len(data[i])) :
			if (lastSign != data[i][k]) :
				lastSign = data[i][k];
				count += 1;
		
	if (data[i][len(data[i]) - 1] == '-') :
		count += 1;

	print("Case #" + str(i + 1) + ": " + str(count));