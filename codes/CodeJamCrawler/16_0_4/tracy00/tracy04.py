pets = raw_input()
pets =int(pets)
cnt=0
for _ in range(pets):
	cnt=cnt+1
	luc,uc,solder = map(int,raw_input().split())
	print("Case #"+str(cnt)+":"),
	for jode in range(1,luc+1):
		print jode,
	print ""
	

