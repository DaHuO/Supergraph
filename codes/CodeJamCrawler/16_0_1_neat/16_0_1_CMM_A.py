def test(N):
	if N == 0: return "INSOMNIA" 
	digits = set(j for j in str(N))
	x = N
	while True:
		x += N
		digits.update(str(x))
		
		if len(digits) == 10:
			return x
			

N = int(raw_input())

case = 1
for i in range(N):
	x = int(raw_input())
	print ("Case #%d:" % case), test(x)
	case += 1
