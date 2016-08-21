f = open('A-large.in.txt')
lines = f.readlines()
f.close()

datas = map(lambda x: x.replace("\n",""), lines)[1:]
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
processed_datas = []

for num in range(len(datas)):
	if num%2 == 1:
		processed_datas.append(datas[num])

ans_lines = []

def solve(data):
	data_list = map(int, data.split(" "))
	ans = ""
	while max(data_list) != 0:
		for num in range(2):
			if max(data_list) != 0:
				max_index = data_list.index(max(data_list))
				data_list[max_index] = data_list[max_index] - 1
				if num == 1:
					if check(data_list):
						ans += alpha[max_index]
					else:
						data_list[max_index] = data_list[max_index] + 1
				else:
					ans += alpha[max_index]
		ans += " "
	ans = ans[:-1]
	return ans

def check(data_list):
	if max(data_list) > sum(data_list)/2:
		return False
	else:
		return True	

# main 
for i, data in enumerate(processed_datas):
	ans_lines.append("Case #"+str(i+1)+": "+"".join(solve(data))+"\n")

f = open('ans.txt', 'w')
for line in ans_lines:
	f.write(line)
f.close() 