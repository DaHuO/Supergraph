import re

def getAnswer(stack):
	purified=re.sub(r'([+-])\1+', r'\1', stack)
	if purified[-1] == "-" : return len(purified)
	return len(purified)-1



for N in range(int(input())) :
	print("Case #"+str(N+1)+": "+str(getAnswer(input())))