remember = {}
def get_digits(N, digits):
	if N in remember:
		return remember[N]
	while (N>0):
		digits[N%10] = True
		N //= 10
	remember[N] = digits
	return digits

def get_output(N, i, digits):
	if N == 0:
		return -1
	digits = get_digits(N*i, digits)
	missing = [x for x in range(10) if not digits[x]]
	if len(missing) > 0:
		return get_output(N, i+1, digits)
	return N*i

def main():
	case = 1
	with open("A-large.in", 'r') as f:
		T = int(f.readline())
		for i in range(T):
			N = int(f.readline())
			num = get_output(N, 1, [False]*10)
			if num == -1:
				num = "INSOMNIA"
			print("Case #{0}: {1}".format(case, num))
			case+=1
			

if __name__ == '__main__':
	main()