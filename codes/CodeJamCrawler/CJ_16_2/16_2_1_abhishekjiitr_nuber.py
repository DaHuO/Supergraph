t = int(input())
for i in range(t):
	hasha = [0 for j in range(100)]
	count = [0 for j in range(10)]
	s = input()
	for ch in s:
		hasha[ord(ch)] += 1
	#print(hasha)

	count[0] = hasha[ord('Z')]
	count[2] = hasha[ord('W')]
	count[6] = hasha[ord('X')]
	count[7] = hasha[ord('S')] - hasha[ord('X')]
	count[5] = hasha[ord('V')] - count[7]
	count[4] = hasha[ord('F')] - count[5]	
	count[1] = hasha[ord('O')] - count[0] - count[2] - count[4]
	count[8] = hasha[ord('G')]
	count[3] = hasha[ord('T')] - count[2] - count[8]
	count[9] = hasha[ord('I')] - count[5] - count[6] - count[8]
	#print(count)
	num = ""
	for i1 in range(10):
		if ( count[i1] > 0 ):
			#print(count[i1])
			for j1 in range(count[i1]): 
				num += str(i1)
	print("Case #%d: %s"%((i+1), num))

