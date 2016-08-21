f = open('B-large.in', 'r')
test_cases = f.readline()
result = []

lines = f.read().split("\n")

for test in range(int(test_cases)):
	flips = 0
	test = lines[test]
	last = test[0]
	for i in range(0, len(test)):
		
		if test[i] == "+" or test[i] == "-":
			if test[i] != last:
				flips += 1
				last = test[i]
	
		if i == len(test)-1:
			
			if test[-1] == "-":
				flips += 1
			
			result.append(flips)

			flips = 0

save = open("output.txt", "w")
for res in range(len(result)):	
	save.write("Case #"+str(res+1)+": "+str(result[res]) + "\n")