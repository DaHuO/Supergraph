def opp(i):
	if i =='+':
		return '-'
	return '+'
def flip(arr, i):
	if i>=len(arr):
		raise ValueError('A very specific bad thing happened')
	arr1 = arr[:i+1]
	arr2 = arr[i+1:]
	arr1 = arr1[::-1]
	# print arr1
	# print arr2
	return ''.join([opp(i) for i in arr1] + list(arr2))
def solve(arr):
	tp = arr[0]
	i = 0
	ans = 0
	while i < len(arr)-1:

		if arr[i+1] == tp:
			i+=1
			# print arr
			continue
		else:
			arr = flip(arr,i)
			i+=1
			tp = arr[0]
			ans +=1
			# print arr
	if arr[0] == '-':
		ans+=1
	return ans


t = int(raw_input())
for _ in range(1,t+1):
	arr = raw_input()
	print("Case #%i: %s" % (_, solve(arr)))