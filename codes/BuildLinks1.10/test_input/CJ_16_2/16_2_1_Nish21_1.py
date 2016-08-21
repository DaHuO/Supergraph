tc = int(input())
for t in range(tc):
	a = input()
	number=''
	times=[0]*10	
	times[0] = a.count('Z')
	times[2] = a.count('W')
	times[4] = a.count('U')
	times[6] = a.count('X')
	times[8] = a.count('G')
	times[1] = a.count('O') - times[0] - times[2] - times[4]
	times[3] = a.count('R') - times[0] - times[4]
	times[5] = a.count('F') - times[4]
	times[7] = a.count('V') - times[5]
	times[9] = a.count('I') - times[5] - times[6] - times[8]
	for i in range(10):
		if times[i] != 0:
			for _ in range(times[i]):
				number += str(i)
	print("Case #"+str(t+1)+": "+number)