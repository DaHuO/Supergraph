f = open('B-large.in.txt')
lines = f.readlines()
f.close()

datas = map(lambda x: x.replace("\n",""), lines)[1:]
ans_lines = []

def join(data):
	data_list = list(data)
	del_index = []
	for i in range(len(data_list)-1):
		try:
			if data_list[i] == data_list[i+1]:
				data_list[i] = ""
		except:
			pass
	data_list = filter(lambda a: a != "", data_list)
	return data_list

def solve(data):
	data_list = join(data)
	if data_list[-1] == "+":
		ans = len(data_list) - 1
	else:
		ans = len(data_list)
	return ans

# main 
for i, data in enumerate(datas):
	ans_lines.append("Case #"+str(i+1)+": "+str(solve(data))+"\n")

f = open('ans.txt', 'w')
for line in ans_lines:
	f.write(line)
f.close() 