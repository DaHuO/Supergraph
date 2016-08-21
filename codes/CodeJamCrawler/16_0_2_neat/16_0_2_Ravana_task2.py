T = int(input())
data = []
for i in range(T):
	data.append(input())

def flip(s):
	return s[::-1].replace("+","!").replace("-","+").replace("!","-")

def bruteflip(s):
	return s.replace("+","!").replace("-","+").replace("!","-")

# ---+-+-+++++-+++-+---+++-+----+++-++
	
def solve(S,res):
	if("-" not in S):
		return res
	
	# find first combo breaker
	
	if(S[0]=="-"):
		i = S.find("+")
	else:
		i = S.find("-")
	if(i==-1):
		i=len(S)
	# print(i)
	# print(flip(S[:i]))
	# input()
	return solve(flip(S[:i])+S[i:],res+1)
	
for case in range(T):
	print("Case #"+str(case+1)+":",solve(data[case],0))
