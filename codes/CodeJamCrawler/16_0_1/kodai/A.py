f = open('A-large.in.txt')
lines = f.readlines()
f.close()

datas = map(lambda x: int(x.replace("\n","")), lines)[1:]
ans_lines = []

def solve(data):
	digit_list = []
	for i in range(100000):
		check = (i+1)*data
		for l in range(len(str(check))):
			digit_list.append(int(str(check)[l]))
		digit_list = list(set(digit_list))
		digit_list.sort()
		if digit_list == [0,1,2,3,4,5,6,7,8,9]:
			return check
	return "INSOMNIA"

# main 
for i, data in enumerate(datas):
	ans_lines.append("Case #"+str(i+1)+": "+str(solve(data))+"\n")

f = open('ans.txt', 'w')
for line in ans_lines:
	f.write(line)
f.close() 