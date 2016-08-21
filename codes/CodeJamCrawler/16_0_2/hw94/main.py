# t = int(raw_input())  # read a line with a single integer
# for i in xrange(1, t + 1):
#   n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
#   print "Case #{}: {} {}".format(i, n + m, n * m)

def flipPancakes(pan,hi):
	ret=[]
	for x in range(0,hi):
		if pan[x]=='+':
			ret.append('-')
		else:
			ret.append('+')
	for x in range(hi,len(pan)):
		ret.append(pan[x])
	return ret

def parse(stack):
	for x in range(0,len(stack)):
		ind=len(stack)-1-x
		if stack[ind]=='-':
			ret = flipPancakes(stack,(len(stack)-x))
			return ret;
	return stack

def checkHappy(pans):
	for s in pans:
		if s=='-':
			return False
	return True 

def pancakes(pan):
	flips=0;
	happy=False
	if checkHappy(pan):
		return 0
	while happy==False:
		pan=parse(pan)
		happy=checkHappy(pan)
		flips+=1;
	return flips




t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n = [str(s) for s in raw_input().split(" ")] 
  n=[c for c in n[0]]
  res = pancakes(n)
  print "Case #{}: {}".format(i, res)



