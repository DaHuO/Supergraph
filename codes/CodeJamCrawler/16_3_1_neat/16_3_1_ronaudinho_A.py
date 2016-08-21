'''
Google Code Jam 2016
Round 1C
Problem A - Senate Evacuation
'''

cases = int(raw_input())

for case in range (cases):
	n = int(raw_input())
	p = raw_input().split(" ")
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	# find total senate members
	total = 0
	for i in range (n):
		total = total + int(p[i])
		p[i] = [int(p[i]), alphabet[i]]
	p.sort(reverse = True)
	
	y = ""
	while total > 0:
		count = 0
		for i in range (n):
			if p[i][0] == p[0][0]:
				count = count + 1
		if count == len(p) and len(p) > 2:
			y = y + p[0][1] + " "
			p[0][0] = p[0][0] - 1
			total = total - 1
			p.sort(reverse = True)
			continue
		else:
			y = y + p[0][1]
			p[0][0] = p[0][0] - 1
			total = total - 1
			if p[1][0] < total / 2:
				y = y + p[0][1] + " "
				p[0][0] = p[0][0] - 1
				total = total - 1
			else:
				y = y + p[1][1] + " "
				p[1][0] = p[1][0] - 1
				total = total - 1
			p.sort(reverse = True)
	
	print ("Case #{}: {}".format(case + 1, y))