cases = int(input())

counter = 0

while counter < cases:
	Str = input()

	win = []
	index = 0
	for x in Str:
		if index == 0:
			win.append(x)
			index+=1
			continue
		if x >= win[0]:
			win.insert(0,x)
			index+=1
		else:
			win.append(x)
			index+=1

	print("Case #" + str(counter+1) + ": " +''.join(win))
	counter += 1