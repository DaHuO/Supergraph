f = open('A-large.in.txt')
lines = f.readlines()
f.close()

datas = map(lambda x: x.replace("\n",""), lines)[1:]
ans_lines = []

def solve(data):
	list_data = list(data)
	ans = [list_data[0]]
	for i in range(len(list_data)-1):
		if list_data[i+1] >= ans[0]:
			ans.insert(0, list_data[i+1])
		else:
			ans.append(list_data[i+1])
	return ans

# main 
for i, data in enumerate(datas):
	ans_lines.append("Case #"+str(i+1)+": "+"".join(solve(data))+"\n")

f = open('ans.txt', 'w')
for line in ans_lines:
	f.write(line)
f.close() 