import fileinput


def countsheep(number) :
	if(int(number) == 0) :
		return "INSOMNIA"

	keep_number = dict()
	new_number = 0
	for cloop in range (1,100):
		new_number = int(number) * cloop
		arr_number = list(str(new_number))
		for each_number in arr_number:
			keep_number[str(each_number)] = ""

		if(len(keep_number) >= 10) :
			return new_number

	return "LIMIT 100"



#if __name__ == "__main__":
# f = open("file.txt", "r")
# T = int(f.readline())
# print T
# for case in range(1,T+1):
# 	num = f.readline()
# 	ans = countsheep(num)
# 	print("Case #{0}: {1}".format(case, ans))

result = open("output2.txt", 'w')

# print fun("152")

# print countsheep("152")
fl = fileinput.input()
total = fl.readline()
#result.write(line1)
#print total
for sheep in  range(1,int(total)+1):
	num = fl.readline()
	count = str(countsheep(num))
	#print("Case #{0}: {1} \n".format(sheep, count))
	result.write("Case #{0}: {1} \n".format(sheep, count))

