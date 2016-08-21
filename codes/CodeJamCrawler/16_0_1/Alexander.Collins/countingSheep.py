#!/usr/local/bin/python3

with open("A-large.in.txt") as f:
    content = f.read().splitlines()

for i in range(1, len(content)):
	N = int(content[i])
	digitsSeen = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
	counter = 1
	result = N * 1

	while( True ):
		# set the seen digits
		for character in str( result ):
			digitsSeen[int(character)] = 1

		# check if all the digits have been seen, if not check for insomnia 
		if( all( digitSeen == True for digitSeen in digitsSeen )):
			print("Case #{}: {}".format(i , result))
			break
		else:
			if( result == (counter + 1) * N ):
				print("Case #{}: INSOMNIA".format(i))
				break
		result = counter * N
		counter += 1
	