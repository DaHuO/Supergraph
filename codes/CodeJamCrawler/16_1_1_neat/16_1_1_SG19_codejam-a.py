def solver(cases):
	with open("codejam-a-large.out", "w") as f:
		for i, c in enumerate(cases, start=1):
			f.write("Case #%d: %s" % (i, helper(c)))
		f.close() 

def helper(phr):
	best_phr = phr[0]
	for ch in phr[1:]:
		if ord(ch) >= ord(best_phr[0]):
			best_phr = ch + best_phr
		else:
			best_phr = best_phr + ch
	return best_phr 

if __name__ == "__main__":
	with open('A-large.in', 'r') as f:
		f.readline()
		cases = f.readlines()
		solver(cases)
		f.close()