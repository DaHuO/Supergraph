def find_last_row(arr):
	hash_dict = {}
	for i in range(len(arr)):
		for j in range(0, len(arr[i])):
			number = arr[i][j]
			if number not in hash_dict: hash_dict[number] = 1
			else: hash_dict[number] = hash_dict[number] + 1
	result = []
	for k,v in hash_dict.items():
		if v % 2 != 0: result.append(k)
	result.sort()
	return result

if __name__ == "__main__":
	t = int(raw_input())
	for i in range(1, t+1):
		length = int(raw_input())
		arr = []
		for j in range(2*length-1):
			nums = map(int, raw_input().split())
			arr.append(nums)
		result = find_last_row(arr)
		res = " ".join(str(x) for x in result)
		print "Case #%d: %s" %(i, res)
