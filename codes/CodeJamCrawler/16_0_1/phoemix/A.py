def isDone(seen):
	for v in seen.values():
		if v == False:
			return False
	return True

if __name__ == "__main__":
	t = int(raw_input())
	
	for i in range(t):
		seen = {'0': False, \
		        '1': False, \
		        '2': False, \
		        '3': False, \
		        '4': False, \
		        '5': False, \
		        '6': False, \
		        '7': False, \
		        '8': False, \
		        '9': False  \
		       }
		n = int(raw_input())
		s = n

		if n == 0:
			print "Case #%d: INSOMNIA" %(i+1)
			continue

		while(not isDone(seen)):
			s_str = str(s)

			for c in s_str:
				seen[c] = True
			s += n
		
		print "Case #%d: %d" %(i+1, s - n)


