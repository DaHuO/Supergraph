import sys
out= sys.stdout.write
t = int(raw_input())
search = [["Z", "ZERO", "0"], ["W", "TWO", "2"], ["X", "SIX", "6"], ["S", "SEVEN", "7"], ["G", "EIGHT", "8"], ["V", "FIVE", "5"], ["I", "NINE", "9"], ["N", "ONE", "1"], ["F", "FOUR", "4"], ["T", "THREE", "3"]]
for x in range(1, t+1):
	number = []
	string = raw_input()
	for check in search:
		instances = string.count(check[0])
		for y in list(check[1]):
			string= string.replace(y,"",instances)
		for z in range(0, instances):
			number += [check[2]]
	number = sorted(number)
	number = "".join(number)
	out("Case #")
	x = str(x)
	out(x)
	out(": ")
	out(number)
	out("\n")

	
		


			
			

