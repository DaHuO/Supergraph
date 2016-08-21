from collections import Counter

for i in range(int(input())):
	dim = int(input())
	all_nums = []
	for j in range(dim*2-1):
		nums = list(map(int, input().split()))
		all_nums.extend(nums)
	c = dict(Counter(all_nums))
	result = sorted([k for k in c if c[k] % 2 == 1])
	print("Case #{}: {}".format(i+1, ' '.join(list(map(str, result)))))