minAttempt = 9

def happy(plate):

	for c in plate:
		if c == False:
			return False
		
	return True


def rec(plate, flipCount, i):
	
	global minAttempt

	if(flipCount > minAttempt  or happy(plate)):
		print(minAttempt)
		if flipCount < minAttempt :
			minAttempt = flipCount
		return

	flip(i, plate)
	
	c = 0
	while(c < len(plate)):
		rec(plate, flipCount + 1, i + c)
		c += 1

	return

def flip(i, plate):

	for c in range(0, i):
		plate[c] = not plate[c]

	return plate



def main():
	
	global minAttempt
	minAttempt = 99999
	plate = [False, False, True, False]

	rec(plate, 0, 0)

	print(flip(2, plate, 1))
main()
