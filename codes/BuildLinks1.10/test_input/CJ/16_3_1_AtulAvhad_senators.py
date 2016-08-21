for _ in range(input()):
	n = int(raw_input())  # total no of parties
	senators = map(int , raw_input().split())
	arr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	empty = [0 for i in range(n)]
	count =0 
	st = ""
	space = " "
	while(senators!=empty):
		
		maxindex = senators.index(max(senators))
		st  += arr[maxindex]
		senators[maxindex] -= 1
		if(max(senators)> sum(senators) - max(senators)):
			maxindex = senators.index(max(senators))
			senators[maxindex] -= 1
			st  += arr[maxindex]

		
		st+=space

	print "Case #"+str(_+1)+": "+st
