def posibleList(list_,j):
	j += 1
	size = len(list_)
	result = list_[0]
	for i in range(1,size):
		if i > 0 :
			if list_[i] >= result[0]:
				result = list_[i] + result 
			else:
				result = result + list_[i]
	print("CASE #" + str(j) + ": " + result)


n = int(input())
for i in range(n):
	str_ = input()
	posibleList(str_,i)