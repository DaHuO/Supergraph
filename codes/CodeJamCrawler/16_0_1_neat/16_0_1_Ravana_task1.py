T = int(input())
data = []
for i in range(T):
	data.append(int(input()))

def solve(n,i,seen):
	if(i==1 and 0 in seen and 1 in seen and 2 in seen and 3 in seen and 4 in seen and 5 in seen and 6 in seen and 7 in seen and 8 in seen and 9 in seen):
		# print("last n:",n*i)
		return n*i
	for c in str(n*i):
		# print("added",c)
		seen.add(int(c))
	if(0 in seen and 1 in seen and 2 in seen and 3 in seen and 4 in seen and 5 in seen and 6 in seen and 7 in seen and 8 in seen and 9 in seen):
		# print("last n:",n*i)
		return n*i
	return solve(n,i+1,seen)

for case in range(T):
	try:
		print("Case #"+str(case+1)+":",solve(data[case],1,set()))
	except:
		print("Case #"+str(case+1)+":","INSOMNIA")