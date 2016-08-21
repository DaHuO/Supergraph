def count(case):
	numbers = [0,1,2,3,4,5,6,7,8,9]
	res = 0

	if case == 0:
		return "INSOMNIA"

	while numbers:
		res += case

		for nr in str(res):
			if int(nr) in numbers:
				numbers.remove(int(nr))
		
	return res



f = open('A-large.in', 'r')
test_cases = f.readline()


save = open("output.txt", "w")	
	

for case in range(int(test_cases)):
	svar = count(int(f.readline()))
	save.write("Case #"+str(case+1)+": "+str(svar) + "\n")