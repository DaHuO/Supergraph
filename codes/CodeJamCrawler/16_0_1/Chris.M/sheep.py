def main():
	f = open('A-large.in', 'r')
	outfile = open('results', 'w')
	case_number = 1
	for line in list(f)[1:]:
		outfile.write('Case #%i: %s\n' %(case_number, check_sleep(int(line))))
		case_number += 1


def check_sleep(N):
	cap = 10000
	seenArray = [False]*10
	a = 0
	while not seen_all(seenArray) and a < cap:
		a += 1
		check_digits(str(a * N), seenArray)
	if a < cap:
		return str(a * N)
	else:
		return 'INSOMNIA'

def check_digits(strn, seenArray):
	for i in range(len(strn)):
		seenArray[int(strn[i])] = True
	
def seen_all(seenArray):
	for i in seenArray:
		if not i:
			return False
	return True
	
main()