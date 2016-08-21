def find(s, arr, num, special_char, whole):
	c = 0
	l = list(s)
	for i in s:
		if i == special_char:
			c += 1

	for i in range(c):
		arr.append(num)
		for w in whole:
			del l[l.index(w)]
	return "".join(l)

n = int(input())
cases = [0] * n
for i in range(n):
	cases[i] = input()

for case in range(n):
	s = cases[case]
	arr = []
	s = s.lower()
	s = find(s, arr, 0, 'z', 'zero')
	s = find(s, arr, 2, 'w', 'two')
	s = find(s, arr, 4, 'u', 'four')
	s = find(s, arr, 6, 'x', 'six')
	s = find(s, arr, 8, 'g', 'eight')
	s = find(s, arr, 5, 'f', 'five')
	s = find(s, arr, 3, 'r', 'three')
	s = find(s, arr, 7, 'v', 'seven')
	s = find(s, arr, 1, 'o', 'one')
	s = find(s, arr, 9, 'i', 'nine')
	
	arr.sort()
	arr_str = "".join(map(str, arr))
	print('Case #' + str(case+1) + ': ' + arr_str)