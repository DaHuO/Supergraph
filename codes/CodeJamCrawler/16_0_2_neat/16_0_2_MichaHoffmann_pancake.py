def signflip(s):
	if s == '+':
		return '-'
	else:
		return '+'

def Flip(pancakes):
	A = []
	t = pancakes[0]
	helper = pancakes
	while t == pancakes[0]:
		A.append(t)
		helper = helper[1:]
		if len(helper) >0:
			t = helper[0]
		else: break
	A = [signflip(t) for t in A]
	B = pancakes[len(A):]
	return A + B

def happysideup(pancakes):
	i = 0 
	while any(t=='-' for t in pancakes):
		i += 1
		pancakes = Flip(pancakes)
	return i
t = int(raw_input())
for i in xrange(1, t + 1):
	pancakes = list(raw_input())
	print "Case #{}: {}".format(i, happysideup(pancakes))

