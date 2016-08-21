#!/usr/bin/env python
if __name__=="__main__":
	
	for i in range(int(raw_input())):
		
		N = int(raw_input())
		dig_map = {i:False  for i in range(10)}
		
		if N == 0:
			print("Case #%d: INSOMNIA" % (i+1))
		else:
			j = 1
			while True:

				# Fill in the dig_map
				temp = j * N
				while temp:
					dig_map[temp % 10] = True
					temp = temp / 10
				
				# check if the dig_map is complete
				dig_seen = sum([int(dig_map[k]) for k in dig_map])
				if dig_seen == 10:
					print("Case #%d: %d" % (i+1, j*N))
					break
				else:
					j += 1