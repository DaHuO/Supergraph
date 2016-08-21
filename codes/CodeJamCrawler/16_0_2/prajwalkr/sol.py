def switchTill(i):
	global a,plus,minus
	for j in range(i + 1):
		a[j] = (minus if a[j] == plus else plus)

def main():
	global a,plus,minus
	t = input()
	plus,minus = '+','-'
	for case in range(t):
		a = list(raw_input())
		prev = len(a) - 1
		res = 0
		while True:
			i = prev
			while i >= 0 and a[i] == plus:
				i -= 1
			if i >= 0:
				switchTill(i)
				res += 1
				prev = i - 1
			else:
				break
		print "Case #{}: {}".format(case + 1,res)
			
main()
